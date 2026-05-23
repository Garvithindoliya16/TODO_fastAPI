from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database.connection import Base

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, nullable=False)
    completed = Column(Boolean, default=False)
    description = Column(String)
    owner_email =Column(String,ForeignKey("users.email"))