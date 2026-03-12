from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

# Define class  (Creating a class)
class Model(BaseModel):
    name: str
    instructor: str
    duration: float
    website: HttpUrl

# Post method
@app.post("/post")                 
def create_post(post: Model):
    return{"data":post}





# Get method
@app.get("/")
def hello():
    return {"message": "Hello from FastAPI!"}


@app.get("/hi")
def hi():
    return {"message": "Hi from FastAPI!"}


@app.get("/api")
def hello():
    return {"message": "Hi from Api"}


@app.get("/django")
def django():
    return {"message": "Hello from django!"}


@app.get("/course")
def course():
    return {"message": "My FastApi Course"}


@app.get("/motivation/code")
def hello():
    return {"message": "Consintency is the only motivation"}