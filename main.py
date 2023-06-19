from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from config.db import conn
from models.contact import Contact,Cart
from schemas.contact import contactEntity, contactsEntity
from schemas.checkoutdb import cartEntity,cartsEntity

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")




@app.get("/", response_class=HTMLResponse)
async def index(request: Request, ):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request, ):
    return templates.TemplateResponse("about.html", {"request": request})


@app.get("/service", response_class=HTMLResponse)
async def service(request: Request, ):
    return templates.TemplateResponse("service.html", {"request": request})


@app.get("/cart", response_class=HTMLResponse)
async def read(request: Request, ):
    docs = conn.cart.cart.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id":doc["_id"],
            # "firstName":doc["firstName"],
            "lastName":doc["lastName"],
            "email":doc["email"],
            "product":doc["product"],
            "address":doc["address"],
            "address2":doc["address2"],
            "country":doc["country"],
            "state":doc["state"],
            "zip":doc["zip"],
            "cc-name":doc["cc-name"],
            "cc-number":doc["cc-number"],
            "cc-expiration":doc["cc-expiration"],
            "cc-cvv":doc["cc-cvv"]
        })
    return templates.TemplateResponse("cart.html", {"request": request, "newDocs":newDocs})

@app.post("/cart")
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)
    cart = conn.cart.cart.insert_one(formDict)
    return{"Your data will be saved into our database": True}

@app.get("/contact", response_class=HTMLResponse)
async def read_item(request: Request, ):
    docs = conn.contacts.contacts.find({})
    newDocs =[]
    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            "email":doc["email"],
            "desc": doc["desc"],
        })
    return templates.TemplateResponse("contact.html", {"request": request, "newDocs":newDocs})

@app.post("/contact")
async def create_item(request: Request):
    form = await request.form()
    formDict =dict(form)
    note = conn.contacts.contacts.insert_one(formDict)
    return {"success": True}