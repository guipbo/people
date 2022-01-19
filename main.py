from dataclasses import dataclass
from fastapi import FastAPI
from markupsafe import re
from pydantic import BaseModel

app = FastAPI()

# Model


class People(BaseModel):
    id: int
    name: str
    cpf: str
    email: str
    phone: str


# Database
_data = [
    People(id=1, name="Joaquim Davi", cpf="45699376240",
           email="joaquimdavi@lphbrasil.com.br", phone="9526674850"),
    People(id=2, name="Milena Jennifer",
           cpf="66628936171", email="milenajennifer@almaquinas.com.br", phone="95998233338")
]

# API


@app.get("/")
async def root():
    return {"message": "Hello, you"}


@app.get("/people")
async def get_all_people():
    return _data


@app.get("/people/{id}")
async def get_people_by_id(id: int):
    for people in _data:
        if(people.id == id):
            return people
    return {"Status": 404, "Message": "Not found"}


@app.post("/people")
async def create_people(people: People):
    _data.append(people)
    return people


@app.put("/people")
async def update_people(updatedPeople: People):
    for people in _data:
        if(people.id == updatedPeople.id):
            _data[_data.index(people)] = updatedPeople
            return updatedPeople
    return {"Status": 404, "Message": "Not found"}


@app.delete("/people/{id}")
async def delete_people(id: int):
    for people in _data:
        if(people.id == id):
            _data.remove(people)
            return people
    return {"Status": 404, "Message": "Not found"}
