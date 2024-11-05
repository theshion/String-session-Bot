from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from Config import DATABASE_URL

print("DATABASE_URL:", DATABASE_URL)  # Debug print to confirm the URL

# Create a declarative base
BASE = declarative_base()

def start() -> scoped_session:
    # Create the database engine
    try:
        engine = create_engine(DATABASE_URL)
        # Bind the metadata to the engine
        BASE.metadata.bind = engine
        # Create all tables if they don't exist
        BASE.metadata.create_all(engine)
        print("Database tables created successfully.")
    except Exception as e:
        print(f"Error creating engine or tables: {e}")
        raise  # Raise the exception to avoid silent failures

    # Return a scoped session
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

# Initialize the session
SESSION = start()
