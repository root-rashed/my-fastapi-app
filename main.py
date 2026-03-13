from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()


# Define class  (Creating a class)
class Model(BaseModel):
    name: str
    instructor: str
    duration: float
    website: HttpUrl


#Databse
while True:
    try:
         conn = psycopg2.connect(host='localhost',database='course',user='postgres',password='YOUR_PASSWORD',cursor_factory=RealDictCursor)
         cursor = conn.cursor()
         print('Database connected sucessfully')
         break
    except Exception as error:
        print('Database connection failed')
        print('Error',error)
        time.sleep(2)






# Post method
@app.post("/post")                 
def create_post(post: Model):
    return{"data":post}


# Get method
@app.get("/")
def hello():
    cursor.execute("""SELECT * FROM course_details""")
    data = cursor.fetchall()
    return {"Data": data}


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