import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# =========================
# PROJECT ROOT SAFE PATH
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Ensure database folder exists
DB_DIR = os.path.join(BASE_DIR, "../database/sqlite")
os.makedirs(DB_DIR, exist_ok=True)

DB_PATH = os.path.join(DB_DIR, "acip_x1.db")

# SQLite URL (absolute path fix for Windows/Linux/Mac)
DATABASE_URL = f"sqlite:///{DB_PATH}"

# =========================
# ENGINE (optimized for SQLite)
# =========================
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # required for FastAPI
    echo=False,  # set True only for debugging SQL logs
    future=True
)

# =========================
# SESSION LOCAL
# =========================
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False  # safer for API responses
)

# =========================
# BASE MODEL
# =========================
Base = declarative_base()

# =========================
# DB DEPENDENCY
# =========================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()