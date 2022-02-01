import os
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from utils.webResponse import createWebResp, errorWebResp

from routers.exchange import router as exchangeRouter
from routers.quotation import router as quotationRouter
from routers.server import router as serverRouter
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

# add Routers
app.include_router(exchangeRouter)
app.include_router(quotationRouter)
app.include_router(serverRouter)

project_version = os.environ['PROJECT_VERSION']


# set openapi
def custom_openapi():
    if app.openapi_schema:
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
    return createWebResp("Hello Upbit Auto Trading.", 200)


# version
@app.get("/version")
def version():
    return createWebResp(project_version, 200)
