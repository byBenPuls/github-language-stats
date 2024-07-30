import uvicorn

from src.main import create_app

if __name__ == "__main__":
    config = uvicorn.Config(create_app(), port=8000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
