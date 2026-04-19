from sqlalchemy import Column,Integer,String,Float
from .database import Base

class Course(Base):
    __tablename__ = "courses"