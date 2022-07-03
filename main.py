import os
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from utils.webResponse import create_web_resp, error_web_resp

from routers.utils import router as utils_router
from routers.exchange import router as exchange_router
from routers.quotation import router as quotation_router
from routers.server import router as server_router
from fastapi.middleware.cors import CORSMiddleware

# define Server
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://152.70.243.130:3000",
    "http://192.168.0.16:3000",
    "http://localhost:8080"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

project_version = os.environ['PROJECT_VERSION']


# set openapi
def custom_openapi():
    if app.openapi_schema:
        print("skip setting openapi-schema.")
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="upbit auto trading",
        version=project_version,
        description="upbit auto trading api document",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


# root
@app.get("/")
def read_root():
    return create_web_resp("Hello Upbit Auto Trading.", 200)


# version
@app.get("/version")
def version():
    return create_web_resp(project_version, 200)


# add Routers
app.include_router(exchange_router)
app.include_router(quotation_router)
app.include_router(server_router)
app.include_router(utils_router)
