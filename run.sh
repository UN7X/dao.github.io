#!/bin/sh
if [ -f ".marker_file" ]; then
    echo "Marker file exists. Skipping setup."
else
    echo "Running setup..."
    pip install -r requirements.txt
    touch .marker_file
fi

uvicorn app.main:app --host 0.0.0.0 --port 8000

