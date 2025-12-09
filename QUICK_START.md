# 🌿 Whisper Web - Quick Start

## Install (Once)
```bash
pip install fastapi uvicorn pydantic
```

## Setup Structure
```bash
# Create static folder
mkdir static

# Move frontend into it
move index.html static/
# Mac/Linux: mv index.html static/
```

## Your Files Should Be:
```
your-folder/
├── my_quotes.json
├── my_quote_embeddings.npy
├── api.py
└── static/
    └── index.html
```

## Run
```bash
python api.py
```

## Visit
Open browser: **http://localhost:8000**

## Stop
Press **Ctrl+C**

---

That's it! 🌿

Type how you're feeling → Quotes from YOUR archive appear.

Dark. Warm. Gentle. Yours.
