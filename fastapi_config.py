import multiprocessing

"""Uvicorn configuration file for running the FastAPI application."""

# Server socket
bind = "0.0.0.0:8000"

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"
worker_connections = 1000
timeout = 30
keepalive = 2

# Process naming
proc_name = "fastapi_api"

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

daemon = False

# Server hooks
def on_starting(server):
    print("Server is starting!")

def on_exit(server):
    print("Server is shutting down!")

