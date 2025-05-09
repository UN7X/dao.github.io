from fastapi import Request, HTTPException

def verify_api_key(request: Request):
    key = request.headers.get("Authorization")
    if key != "Bearer supersecret":  # replace later with env load
        raise HTTPException(status_code=401, detail="Unauthorized")
