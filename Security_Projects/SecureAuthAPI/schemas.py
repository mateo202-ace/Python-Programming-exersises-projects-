from pydantic import BaseModel

class UserBase(BaseModel): 
    username: str
    email: str


""" This class is the base class for the User class. It has two
attributes: username and email. Both attributes are of type str. """

class UserCreate(UserBase): 
    password: str


class User(UserBase):
    id: int

    class Config: 
        orm_mode = True