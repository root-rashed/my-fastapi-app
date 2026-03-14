from fastapi import FastAPI,HTTPException,status,responses,Response
from pydantic import BaseModel, HttpUrl
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()


# Define class  (Creating a class)
class Model(BaseModel):
    name: str
    instructor: str
    duration: int
    website: HttpUrl


#Databse
while True:
    try:    
         conn = psycopg2.connect(host='localhost',database='course',user='postgres',password='PASSWORD',cursor_factory=RealDictCursor)
         cursor = conn.cursor()
         print('Database connected sucessfully')
         break
    except Exception as error:
        print('Database connection failed')
        print('Error',error)
        time.sleep(2)





@app.get("/course/{id}")
def details(id: int):
    cursor.execute("""SELECT * FROM course_details WHERE id=%s""", (str(id),))  # ✅ tuple
    course = cursor.fetchone()   # ✅ renamed + added ()

    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Course with id:{id} not found")
    return {"Course details": course}


@app.post("/post")
def create_post(post: Model):
    cursor.execute("""INSERT INTO course_details(name,instructor,duration,website) VALUES (%s,%s,%s,%s) RETURNING *""",
                   (post.name, post.instructor, post.duration, str(post.website)))
    new_post = cursor.fetchone()   # ✅ added ()
    conn.commit()
    return {"Data": new_post}



@app.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_course(id: int):
    cursor.execute("""DELETE FROM course_details WHERE id=%s RETURNING *""", (str(id),))
    deleted = cursor.fetchone()
    conn.commit()

    if deleted is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Course with id:{id} not found")
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)  # ✅ correct status



@app.put("/update/{id}", status_code=status.HTTP_200_OK)
def update_course(id: int, post: Model):
    cursor.execute("""UPDATE course_details SET name=%s, instructor=%s, duration=%s, website=%s WHERE id=%s RETURNING *""",
                   (post.name, post.instructor, post.duration, str(post.website), str(id)))
    updated = cursor.fetchone()
    conn.commit()

    if updated is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Course with id:{id} not found")
    
    return {"Data": updated}












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