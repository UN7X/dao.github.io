if [ -f ".marker_file" ]; then
    echo "Marker file exists. Skipping setup."
else
    echo "Running setup..."
    pip install -r requirements.txt
    touch .marker_file
fi

gunicorn app.main:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
