import os

import uvicorn


if __name__ == "__main__":
    uvicorn.run('src.main:app', host=os.getenv('APP_IP'), port=int(os.getenv('APP_PORT')))
