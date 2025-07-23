from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from main import get_status

class LockdownMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        status = get_status()
        if status.get("lock", True):
            return JSONResponse(
                status_code=403,
                content={"error": "App is locked", "message": status.get("message", "Unauthorized usage.")}
            )
        return await call_next(request)
