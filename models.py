from sqlalchemy import Column,Integer,String,Float
from . databse import Base

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer,primary_key=True,Index = True)
    name = Column(String,nullable=False)
    instructor =Column(String,nullable=False)
    duration = Column(Float,nullable=False)
    website = Column(String,nullable=False)