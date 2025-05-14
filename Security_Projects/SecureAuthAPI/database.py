from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a new database
DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}) # check_same_thread=False is only for SQLite
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # this is the session object

Base = declarative_base() # this is the base class for the models

# Define the user model table
class User(Base):
    __tablename__ = "users" # this is the table name
    id = Column(Integer, primary_key=True, index=True) # this is the id 
    username = Column(String, unique=True, index=True) # this is the username
    email = Column(String, unique=True, index=True) # this is the email)
    password_hash = Column(String) # this is the hashed password

#create the tables in the database
def init_db():
    Base.metadata.create_all(bind=engine) # this will create the tables in the database