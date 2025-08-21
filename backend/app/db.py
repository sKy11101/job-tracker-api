from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Database URL (fallback to SQLite if not provided)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./jobs.db")

# Engine
engine = create_engine(DATABASE_URL, echo=True, future=True)

# Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# ✅ Dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

