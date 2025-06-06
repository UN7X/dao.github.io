import os
import sys
import subprocess
from pathlib import Path
import importlib.util

REQUIREMENTS_FILE = "requirements.txt"
MARKER_FILE = ".setup_done"


def check_dependencies():
    missing = []
    if os.path.exists(REQUIREMENTS_FILE):
        with open(REQUIREMENTS_FILE) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    pkg = line.split('==')[0]
                    if importlib.util.find_spec(pkg) is None:
                        missing.append(pkg)
    return missing


def create_script(content, filename):
    with open(filename, 'w', newline='') as f:
        f.write(content)
    if os.name != 'nt':
        subprocess.run(['chmod', '+x', filename], check=False)


def main():
    if os.path.exists(MARKER_FILE):
        print("Setup already completed.")
        return

    missing = check_dependencies()
    if missing:
        print("Missing dependencies detected: {}".format(', '.join(missing)))
        print("Please run: pip install -r {}".format(REQUIREMENTS_FILE))
    else:
        print("All dependencies satisfied.")

    if os.name == 'nt':
        content = (
            "@echo off\n"
            "IF EXIST \".marker_file\" (\n"
            "    echo Marker file exists, skipping setup.\n"
            ") ELSE (\n"
            "    echo Marker file does not exist, running setup...\n"
            "    pip install -r requirements.txt\n"
            "    echo Setup completed > .marker_file\n"
            ")\n"
            "echo Starting server with Uvicorn...\n"
            "uvicorn app.main:app --host 0.0.0.0 --port 8000\n"
        )
        script_name = 'run.bat'
    else:
        content = (
            "#!/bin/sh\n"
            "if [ -f \".marker_file\" ]; then\n"
            "    echo \"Marker file exists. Skipping setup.\"\n"
            "else\n"
            "    echo \"Running setup...\"\n"
            "    pip install -r requirements.txt\n"
            "    touch .marker_file\n"
            "fi\n\n"
            "uvicorn app.main:app --host 0.0.0.0 --port 8000\n"
        )
        script_name = 'run.sh'

    create_script(content, script_name)
    Path(MARKER_FILE).touch()
    print(f"Created {script_name}. Run it to start the server.")
    print("Setup completed.")


if __name__ == '__main__':
    main()

