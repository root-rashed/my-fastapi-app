from fastapi import FastAPI, HTTPException, status, Response, Depends,APIRouter
from sqlalchemy.orm import Session
from .. import models,schemas,utils 
from .. database import get_db
from typing import List


router = APIRouter()


# For Users only
@router.post("/users",status_code=status.HTTP_201_CREATED,response_model=schemas.UserRes)
def users(user:schemas.UserCreate,db:Session=Depends(get_db)):
    if db.query(models.User).filter(models.User.email == user.email).first():
                    raise HTTPException(400,"Email Already Exist")                                                                                                                        )
    
    hashed_password = utils.hash_password(user.password)

    user.password = hashed_password
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
