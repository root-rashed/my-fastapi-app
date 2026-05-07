from pydantic import BaseModel, HttpUrl, ConfigDict

class CourseCreate(BaseModel):
    name: str
    instructor: str
    duration: float
    website: HttpUrl


class CourseResponse(CourseCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)