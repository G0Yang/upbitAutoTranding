from dotenv import load_dotenv
import os
import uvicorn

load_dotenv()

try:
    HOST_IP = os.environ.get('HOST_IP')
except:
    HOST_IP = "0.0.0.0"

try:
    HOST_PORT = os.environ.get('HOST_PORT')
except:
    HOST_PORT = 8000

try:
    HOST_THREAD = os.environ.get('HOST_THREAD')
except:
    HOST_THREAD = 1

try:
    LOG_LEVEL = os.environ.get('LOG_LEVEL')
except:
    LOG_LEVEL = "info"


def init():
    return os.environ.get('HOST_IP') \
           and os.environ.get('HOST_PORT') \
           and os.environ.get('HOST_THREAD') \
           and os.environ.get('LOG_LEVEL') \
           and os.environ.get('UPBIT_OPEN_API_VERSION') \
           and os.environ.get('UPBIT_OPEN_API_MINOR_VERSION') \
           and os.environ.get('UPBIT_OPEN_API_SERVER_URL') \
           is not None


if __name__ == "__main__":
    if init():
        uvicorn.run(
            app="main:app",
            host=str(os.environ.get('HOST_IP')),
            port=int(os.environ.get('HOST_PORT')),
            reload=True,
            env_file='.env',
            workers=int(os.environ.get('HOST_THREAD')),
            log_level=os.environ.get('LOG_LEVEL'),
        )
