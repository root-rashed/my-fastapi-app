from pydantic import BaseModel, HttpUrl, ConfigDict,EmailStr

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