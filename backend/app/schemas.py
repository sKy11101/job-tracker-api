from pydantic import BaseModel, AnyUrl, Field
from typing import Optional
from datetime import date

class JobBase(BaseModel):
    title: str = Field(..., min_length=1)
    company: str = Field(..., min_length=1)
    platform: Optional[str] = None
    job_url: Optional[str] = None
    date_applied: Optional[date] = None
    status: Optional[str] = "Applied"
    notes: Optional[str] = None

class JobCreate(JobBase):
    pass

class Job(JobBase):
    job_id: int
    class Config:
        from_attributes = True  # Pydantic v2

