from pydantic import BaseModel


class userApiKey(BaseModel):
    access_key: str
    secret_key: str
