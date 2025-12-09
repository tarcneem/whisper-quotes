# 🌿 Whisper Web Interface - Setup Guide

Transform Whisper from terminal to sanctuary.

---

## What You're Building

A beautiful, minimal web interface where:
- You type how you're feeling
- Quotes from YOUR archive fade in gently
- Dark, warm, breathing space
- Works on any device
- Shareable with others

---

## Setup (5 Minutes)

### Step 1: Install Web Dependencies

```bash
pip install fastapi uvicorn pydantic
```

### Step 2: Create Project Structure

Your folder should look like:
```
your-project/
├── my_quotes.json              ← Your 321 quotes (you have this!)
├── my_quote_embeddings.npy     ← Your embeddings (you have this!)
├── api.py                      ← Backend (download)
├── index.html                  ← Frontend (download)
└── requirements_web.txt        ← Dependencies (download)
```

### Step 3: Create Static Folder

The frontend needs to be in a folder called `static`:

```bash
# Create folder
mkdir static

# Move index.html into it
move index.html static/
# Or on Mac/Linux: mv index.html static/
```

Your structure becomes:
```
your-project/
├── my_quotes.json
├── my_quote_embeddings.npy
├── api.py
├── static/
│   └── index.html
```

---

## Running Whisper

### Start the Server

```bash
python api.py
```

You should see:
```
🌿 Loading Whisper...
✅ Loaded 321 quotes
🌿 Whisper API ready

🌿 Starting Whisper API...
Visit: http://localhost:8000

Press Ctrl+C to stop
```

### Open in Browser

Go to: **http://localhost:8000**

---

## Using Whisper

1. **The page loads** - dark, warm, minimal
2. **Type how you're feeling** - "lonely", "stuck", "almost"
3. **Wait 1.5 seconds** - or press Enter
4. **Quotes fade in** - from YOUR archive
5. **Read, breathe** - no rush

---

## What's Happening Behind the Scenes

### The Backend (api.py)
- FastAPI server running on port 8000
- Loads your quotes and embeddings
- Provides `/search` endpoint
- Returns matching quotes with similarity scores

### The Frontend (index.html)
- Single-page interface
- Sends search requests to API
- Displays results with gentle animations
- No page reloads, smooth experience

---

## Customization

### Change Colors

Edit `index.html`, look for:
```css
:root {
    --bg: #0a0807;        /* Background (dark warm brown) */
    --text: #e8e3df;      /* Text (soft warm white) */
    --text-dim: #9a8f86;  /* Dimmed text */
    --accent: #8b9d83;    /* Accent (muted sage) */
}
```

### Change Fonts

In `<head>` section, replace Google Fonts link:
```html
<link href="https://fonts.googleapis.com/css2?family=YOUR_FONT&display=swap">
```

Then update CSS:
```css
font-family: 'Your Font', serif;
```

### Change Number of Results

In `index.html`, line ~173:
```javascript
top_k: 3,  // Change to 5, 10, etc.
```

### Change Search Delay

In `index.html`, line ~189:
```javascript
}, 1500); // Change to 2000 for 2 seconds, etc.
```

---

## Sharing With Others

### Option 1: Run Locally, Share Screen
- Show friends over video call
- They see your screen

### Option 2: Deploy Online (Advanced)
Later we can deploy to:
- Vercel (free, easy)
- Railway (free tier)
- Your own server

For now, keep it local and personal.

---

## Mobile Access

### On Your Phone (Same WiFi)

1. Find your computer's IP address:
   ```bash
   # Windows
   ipconfig
   # Look for IPv4 Address (e.g., 192.168.1.5)
   
   # Mac
   ifconfig | grep "inet "
   ```

2. On your phone's browser, visit:
   ```
   http://YOUR_IP_ADDRESS:8000
   ```
   Example: `http://192.168.1.5:8000`

3. Now you can use Whisper at 2am from your phone in bed 🌿

---

## Troubleshooting

### "Connection refused"
→ Make sure `python api.py` is running

### "No module named 'fastapi'"
→ Run: `pip install fastapi uvicorn`

### "File not found: index.html"
→ Make sure index.html is in `static/` folder

### Page loads but search doesn't work
→ Check browser console (F12) for errors
→ Make sure API is running on port 8000

### Want to stop the server
→ Press `Ctrl+C` in the terminal

---

## The Experience

### At 2am, when you can't sleep:

1. Open `http://localhost:8000` on your phone
2. Dark screen, soft light
3. Type: "can't sleep"
4. Wait for the words to appear
5. Read a quote YOU saved years ago
6. Feel seen
7. Breathe

**That's restoration.**

---

## Next Steps

Once this works:
- **Add voice** - speak instead of type
- **Add memory** - "last time you felt this..."
- **Add saves** - build a collection of quotes that helped
- **Deploy** - share with others
- **Customize** - make it truly yours

But for now:

**Just use it.** 🌿

Feel something → Type it → Find words → Restore.

---

## Files You Need

1. [api.py](computer:///mnt/user-data/outputs/api.py) - Backend
2. [index.html](computer:///mnt/user-data/outputs/index.html) - Frontend
3. [requirements_web.txt](computer:///mnt/user-data/outputs/requirements_web.txt) - Dependencies

Download all three, follow the setup above, and you'll have Whisper in your browser.

---

*"We do not escape into art—we go there to restore our shattered selves into whole ones."*

Your restoration chamber is ready. 💚
