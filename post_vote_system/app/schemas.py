from typing import Optional

from pydantic import BaseModel, conint
from datetime import datetime

from pydantic import EmailStr


class PostBase(BaseModel):
    title:str
    content:str
    published:bool=True
class CreatePost(PostBase):
    pass
class usersOut(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime
    class Config:
        from_attributes = True
class Post(PostBase):
    id:int
    created_at:datetime
    owner_id:int
    owner: usersOut
    class Config:
        from_attributes = True
class Users(BaseModel):
    email:EmailStr
    password:str
    # created_at:datetime
    class Config:
        from_attributes = True
class User_Login(BaseModel):
    email: EmailStr
    password:str
    class Config:
        from_attributes = True
class Token(BaseModel):
    access_token:str
    token_type:str
class TokenData(BaseModel):
    id:Optional[str]=None
class Vote(BaseModel):
    post_id:int
    dir:conint(le=1) #to validate the votes but can have negative because of le


