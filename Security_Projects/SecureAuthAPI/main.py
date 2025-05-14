from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import init_db, SessionLocal, User
from . import crud, schemas

app = FastAPI()

@app.on_event("startup") # this will run the init_db function when the app starts
def startup(): 
    # initialize the database
    init_db() 

@app.get("/") # this is the root path
def read_root(): 
    # this is the function that will run when the root path is accessed
    return {"message": "Welcome to the Authentification API"} 

def get_db():
    """ This function returns a database session. """
    db = SessionLocal() 
    try: 
        yield db 
    finally: 
        db.close()

app.post("/users/", response_model=schemas.User) # this is the path to create a new user
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """ This function creates a new user.
    It takes a UserCreate object as input and returns a User object. """
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user: 
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/{user_id}", response_model=schemas.User) # this is the path to get a user by id
def read_user(user_id: int, db: Session = Depends(get_db)):
    """ This function retrieves a user by its id. """
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None: 
        raise HTTPException(status_code=404, detail="User not found")
    return db_user