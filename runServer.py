import os
import uvicorn

try:
    HOST_IP = os.environ['HOST_IP']
except:
    HOST_IP = "0.0.0.0"

try:
    HOST_PORT = os.environ['HOST_PORT']
except:
    HOST_PORT = 8000

try:
    HOST_THREAD = os.environ['HOST_THREAD']
except:
    HOST_THREAD = 1

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=str(HOST_IP),
        port=int(HOST_PORT),
        reload=True,
        env_file='.env',
        workers=int(HOST_THREAD),
        # log_level= uvicorn,
    )
