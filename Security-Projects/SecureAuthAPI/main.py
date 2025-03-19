from fastapi import FastAPI
from database import init_db


app = FastAPI()

@app.on_event("startup") # this will run the init_db function when the app starts
def startup(): 
    # initialize the database
    init_db() 

@app.get("/") # this is the root path
def read_root(): 
    # this is the function that will run when the root path is accessed
    return {"message": "Welcome to the Authentification API"} 