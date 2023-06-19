from pydantic import BaseModel

class Contact(BaseModel):
    email: str
    desc: str

class Cart(BaseModel):

        firstName:str
        latName:str
        email:str
        product:str
        address:str
        address2:str
        country:str
        state:str
        zip:str
       
       
    