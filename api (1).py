"""
Whisper API - Backend for web interface
Serves your personal quote archive
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Optional

# Initialize FastAPI
app = FastAPI(title="Whisper API")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model and data at startup
print("🌿 Loading Whisper...")

# Load quotes
with open('my_quotes.json', 'r', encoding='utf-8') as f:
    quotes = json.load(f)

# Load embeddings
embeddings = np.load('my_quote_embeddings.npy')

# Load model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

print(f"✅ Loaded {len(quotes)} quotes")
print("🌿 Whisper API ready\n")

# Request/Response models
class SearchRequest(BaseModel):
    query: str
    top_k: Optional[int] = 3
    threshold: Optional[float] = 0.0

class Quote(BaseModel):
    id: int
    text: str
    author: str
    source: Optional[str]
    similarity: float

class SearchResponse(BaseModel):
    query: str
    results: List[Quote]
    count: int

# API endpoints
@app.get("/")
def root():
    """Health check"""
    return {
        "status": "alive",
        "message": "Whisper API is running",
        "quotes": len(quotes)
    }

@app.post("/search", response_model=SearchResponse)
def search(request: SearchRequest):
    """
    Search for quotes matching the emotional tone of the query
    """
    
    if not request.query or not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    
    # Generate embedding for query
    query_embedding = model.encode([request.query])
    
    # Calculate similarity
    similarities = cosine_similarity(query_embedding, embeddings)[0]
    
    # Get top K indices
    top_indices = np.argsort(similarities)[-request.top_k:][::-1]
    
    # Build results
    results = []
    for idx in top_indices:
        similarity = float(similarities[idx])
        
        if similarity < request.threshold:
            continue
        
        quote = quotes[idx]
        
        # Clean up obvious OCR errors
        text = quote['text'].replace('|', 'I').replace('alI', 'all')
        
        results.append(Quote(
            id=quote['id'],
            text=text,
            author=quote['author'],
            source=quote.get('source'),
            similarity=round(similarity, 3)
        ))
    
    return SearchResponse(
        query=request.query,
        results=results,
        count=len(results)
    )

@app.get("/stats")
def stats():
    """Get collection statistics"""
    authors = [q['author'] for q in quotes]
    unique_authors = len(set(authors))
    unknown_count = sum(1 for a in authors if a == "Unknown")
    
    return {
        "total_quotes": len(quotes),
        "unique_authors": unique_authors,
        "quotes_with_known_authors": len(quotes) - unknown_count,
        "model": "sentence-transformers/all-MiniLM-L6-v2"
    }

@app.get("/whisper", response_class=HTMLResponse)
def serve_whisper():
    """Serve the Whisper interface"""
    try:
        with open('whisper_with_voice.html', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return """
        <html>
        <body style="background: #0a0807; color: #e8e3df; font-family: serif; padding: 40px; text-align: center;">
            <h1>🌿 Whisper</h1>
            <p>File 'whisper_with_voice.html' not found in the same directory as api.py</p>
        </body>
        </html>
        """

if __name__ == "__main__":
    import uvicorn
    print("\n🌿 Starting Whisper API...")
    print("Visit: http://localhost:8000/whisper")
    print("\nPress Ctrl+C to stop\n")
    uvicorn.run(app, host="0.0.0.0", port=8000)
