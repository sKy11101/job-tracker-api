import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import Base, engine
from .routers import health, jobs

# Create tables automatically
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Tracker API (MVP)")

# CORS
origins = [os.getenv("ALLOWED_ORIGINS", "http://localhost:5173")]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route
@app.get("/")
def root():
    return {"message": "Job Tracker API is running!"}

# Routers
app.include_router(health.router)
app.include_router(jobs.router)

