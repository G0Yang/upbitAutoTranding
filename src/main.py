from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from routers.exchange import router as exchangeRouter
from routers.quotation import router as quotationRouter

# define Server
app = FastAPI()

# add Routers
app.include_router(exchangeRouter)
app.include_router(quotationRouter)

# root
@app.get("/")
def read_root():
    return "Hello Upbit Auto Trading."

# version
@app.get("/version")
def version():
    return "v0.0.1"

