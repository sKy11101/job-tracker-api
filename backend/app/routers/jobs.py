from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..db import get_db
from .. import models, schemas

router = APIRouter(prefix="/jobs", tags=["jobs"])

@router.post("", response_model=schemas.Job, status_code=201)
def create_job(payload: schemas.JobCreate, db: Session = Depends(get_db)):
    job = models.Job(**payload.model_dump())
    db.add(job)
    db.commit()
    db.refresh(job)
    return job

@router.get("", response_model=List[schemas.Job])
def list_jobs(db: Session = Depends(get_db), status: str | None = None, q: str | None = None):
    query = db.query(models.Job)
    if status:
        query = query.filter(models.Job.status.ilike(status))
    if q:
        like = f"%{q}%"
        query = query.filter((models.Job.title.ilike(like)) | (models.Job.company.ilike(like)))
    return query.order_by(models.Job.job_id.desc()).all()

