from pydantic import BaseModel


class UserApiKey(BaseModel):
    access_key: str
    secret_key: str
