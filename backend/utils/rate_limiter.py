
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
import time

RATE_LIMIT = 100  # Max requests per IP per 10 minutes
WINDOW = 600      # 10 minutes in seconds
requests_store = {}

class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        current_time = time.time()

        if client_ip not in requests_store:
            requests_store[client_ip] = []

        request_times = requests_store[client_ip]
        request_times = [t for t in request_times if t > current_time - WINDOW]

        if len(request_times) >= RATE_LIMIT:
            return Response("Rate limit exceeded", status_code=429)

        request_times.append(current_time)
        requests_store[client_ip] = request_times

        return await call_next(request)
