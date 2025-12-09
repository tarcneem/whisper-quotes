#!/bin/bash
# Start script for Whisper on Render

echo "🌿 Starting Whisper..."
uvicorn api:app --host 0.0.0.0 --port $PORT
