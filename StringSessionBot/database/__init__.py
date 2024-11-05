# StringSessionBot/database/__init__.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from Config import DATABASE_URL  # Import DATABASE_URL from Config.py

# Initialize the base and engine
BASE = declarative_base()

def start() -> scoped_session:
    # Create the database engine using DATABASE_URL
    engine = create_engine(DATABASE_URL)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)  # Create tables
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

# Start the session
SESSION = start()
