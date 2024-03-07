import uvicorn
from fastapi import FastAPI

from src.api import include_routers

app = FastAPI(title="Fast API - todo list")
include_routers(app)

if __name__ == '__main__':
    config = uvicorn.Config("app:app", host="localhost", port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
