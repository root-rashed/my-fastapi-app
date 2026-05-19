from fastapi import FastAPI, HTTPException, status, Response, Depends,APIRouter
from sqlalchemy.orm import Session
from .. import models,schemas  
from .. database import get_db
from typing import List



router = APIRouter()





#  ── SQLAlchemy route ──────────────────────────────────────────────────────────
@router.get("/courses",response_model=list[schemas.CourseResponse])
def course_alchemy(db: Session = Depends(get_db)):
   courses = db.query(models.Course).all()
   return courses


@router.get("/course/{id}",response_model=schemas.CourseResponse)
def course_alchemy(id: int, db: Session = Depends(get_db)):
    courses = db.query(models.Course).filter(models.Course.id == id).first()

    if not courses:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id:{id} not found"
        )
    
    return courses









@router.post("/create_course", response_model=schemas.CourseResponse)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):

    course_data = course.model_dump()
    course_data["website"] = str(course_data["website"])

    new_course = models.Course(**course_data)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return new_course









@router.put("/update_course/{id}")
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



@router.delete("/delete_course/{id}",status_code = status.HTTP_204_NO_CONTENT)
def delete_course(id:int,db:Session=Depends(get_db)):
    course_query = db.query(models.Course).filter(models.Course.id == id)
    course = course_query.first()
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id:{id} not found"
        )
    course_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


