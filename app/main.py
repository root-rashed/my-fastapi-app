from fastapi import FastAPI, HTTPException, status, Response, Depends
from pydantic import BaseModel, HttpUrl
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models
from sqlalchemy.orm import Session  
from .database import engine, get_db  


app = FastAPI()

# Table creation
models.Base.metadata.create_all(bind=engine)


# Pydantic model
class CourseModel(BaseModel):
    name: str
    instructor: str
    duration: int
    website: HttpUrl


# Database connection (raw psycopg2)
conn = None
cursor = None

def connect_db():
    global conn, cursor
    while True:
        try:
            conn = psycopg2.connect(
                host='localhost',
                database='courses',
                user='postgres',
                password='371946852R',
                cursor_factory=RealDictCursor
            )
            cursor = conn.cursor()
            print('Database connected successfully')
            break
        except Exception as error:
            print('Database connection failed')
            print('Error:', error)
            time.sleep(2)

connect_db()


# ── SQLAlchemy route ──────────────────────────────────────────────────────────
@app.get("/coursealchemy")
def course_alchemy(db: Session = Depends(get_db)):
   course = db.query(models.Course).all()
   return {"Course": course}

@app.get("/coursealchemy/{id}")
def course_alchemy(id: int, db: Session = Depends(get_db)):
    course = db.query(models.Course).filter(models.Course.id == id).first()
    
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id:{id} not found"
        )
    
    return {"Course details": course}


@app.post("/courses")
def create_course(course:CourseModel, db:Session = Depends(get_db)):
    new_course = models.Course(
        name = course.name,
        instructor = course.instructor,
        duration = course.duration,
        website = str(course.website)
    )
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return {"Course: ",new_course}


@app.put("/coursealchemy/{id}")
def update_course(id: int, updated_course: CourseModel, db: Session = Depends(get_db)):
    course_query = db.query(models.Course).filter(models.Course.id == id)
    course = course_query.first()
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id:{id} not found"
        )
    update_data = updated_course.model_dump()
    update_data["website"] = str(update_data["website"])  # Fixed: update_date → update_data
    course_query.update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(course)
    return {"Course_details": course}


# ── psycopg2 routes ───────────────────────────────────────────────────────────

@app.get("/")
def get_all_courses(): 
    cursor.execute("""SELECT * FROM course_details""")
    data = cursor.fetchall()
    return {"Data": data}


@app.get("/hi")
def hi():
    return {"message": "Hi from FastAPI!"}


@app.get("/api")
def hello_api(): 
    return {"message": "Hi from Api"}


@app.get("/django")
def django():
    return {"message": "Hello from django!"}


@app.get("/course")
def get_course():  
    return {"message": "My FastApi Course"}


@app.get("/motivation/code")
def motivation():  
    return {"message": "Consistency is the only motivation"}


@app.get("/course/{id}")
def get_course_details(id: int):  
    cursor.execute("""SELECT * FROM course_details WHERE id=%s""", (str(id),))
    course = cursor.fetchone()

    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id:{id} not found"
        )
    return {"Course details": course}


@app.post("/post", status_code=status.HTTP_201_CREATED)
def create_course(post: CourseModel):  
    cursor.execute(
        """INSERT INTO course_details(name, instructor, duration, website)
           VALUES (%s, %s, %s, %s) RETURNING *""",
        (post.name, post.instructor, post.duration, str(post.website))
    )
    new_post = cursor.fetchone()
    conn.commit()
    return {"Data": new_post}


@app.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_course(id: int):
    cursor.execute("""DELETE FROM course_details WHERE id=%s RETURNING *""", (str(id),))
    deleted = cursor.fetchone()
    conn.commit()

    if deleted is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id:{id} not found"
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/update/{id}", status_code=status.HTTP_200_OK)
def update_course(id: int, post: CourseModel): 
    cursor.execute(
        """UPDATE course_details
           SET name=%s, instructor=%s, duration=%s, website=%s
           WHERE id=%s RETURNING *""",
        (post.name, post.instructor, post.duration, str(post.website), str(id))
    )
    updated = cursor.fetchone()
    conn.commit()

    if updated is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id:{id} not found"
        )
    return {"Data": updated}