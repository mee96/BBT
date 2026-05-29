import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

HOST = os.getenv("HOST", "")
PORT = os.getenv("PORT", "3306")
DB = os.getenv("DB", "")
USER = os.getenv("USER", "")
PASSWORD = os.getenv("PASSWORD", "")
CHARSET = os.getenv("CHARSET", "utf8mb4")

DATABASE_URL = (
    f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}?charset={CHARSET}"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600,
    echo=False,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
