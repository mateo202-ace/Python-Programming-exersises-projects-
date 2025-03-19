from sqlalchemy import create_engine, column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a new database
DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}) # check_same_thread=False is only for SQLite
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # this is the session object

Base = declarative_base()

# Define the user model table
class User(Base):
    __tablename__ = "users" # this is the table name
    id = column(Integer, primary_key=True, index=True) # this is the id 
    username = column(String, unique=True, index=True) # this is the username
    password_hash = column(String) # this is the hashed password

#create the tables in the database
def init_db():
    Base.metadata.create_all(bind=engine) # this will create the tables in the database