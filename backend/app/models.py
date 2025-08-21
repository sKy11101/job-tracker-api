from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(150), unique=True, index=True)
    password_hash = Column(Text, nullable=True)  # will add auth later

    jobs = relationship("Job", back_populates="user")

class Job(Base):
    __tablename__ = "jobs"
    job_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)  # null for now
    title = Column(String(150))
    company = Column(String(150))
    platform = Column(String(100))
    job_url = Column(Text)
    date_applied = Column(Date, nullable=True)
    status = Column(String(50), default="Applied")
    notes = Column(Text, nullable=True)

    user = relationship("User", back_populates="jobs")

