from pydantic import BaseModel, HttpUrl, ConfigDict,EmailStr
from datetime import datetime

class CourseCreate(BaseModel):
    name: str
    instructor: str
    duration: float
    website: HttpUrl

class CourseResponse(CourseCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)





class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserRes(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)



class Userlogin(BaseModel):
    email : EmailStr
    password : str