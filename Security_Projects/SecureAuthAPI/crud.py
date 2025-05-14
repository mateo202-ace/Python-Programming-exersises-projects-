from sqlalchemy.orm import Session
from . import models, schemas


def get_user(db: Session, user_id: int):
    """ This function retrieves a user from the database by its id. """
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    """ This function retrieves a user from the database by its username. """
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    """ This function retrieves a user from the database by its email. """
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    """ This function creates a user in the database. """
    db_user = models.User(username=user.username, email=user.email, pasword_hash=user.password_hash)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user