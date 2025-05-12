@echo off
IF EXIST ".marker_file" (
    echo Marker file exists, skipping setup.
) ELSE (
    echo Marker file does not exist, running setup...
    REM Create a marker file to indicate setup has been done
    pip install -r requirements.txt
    echo Setup completed > .marker_file
)
echo Starting server with Uvicorn...
uvicorn app.main:app --host 0.0.0.0 --port 8000