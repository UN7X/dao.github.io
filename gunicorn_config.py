import multiprocessing

# Gunicorn configuration file
# https://docs.gunicorn.org/en/stable/configure.html

# Server socket
bind = "0.0.0.0:8000"  # Use "unix:/path/to/socket" for Unix socket

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"  # Use "gevent" or "uvicorn.workers.UvicornWorker" for async
worker_connections = 1000
timeout = 30
keepalive = 2

# Process naming
proc_name = "gunicorn_api"

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Server mechanics
daemon = False
raw_env = [
    "FLASK_APP=app:create_app()",
    "FLASK_ENV=production"
]

# Server hooks
def on_starting(server):
    print("Server is starting!")

def on_exit(server):
    print("Server is shutting down!")