from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/get/{id}")
def get_name(id: int):
    return {'data': {id: 'maha'}}

@app.get("/about")
def about(company_name,location):
    return {'data': {'company_name':company_name,'location': location}}

class item(BaseModel):
    name : str
    company_name :str
    company_location:str
    designation: str
    is_present : Optional[bool]

@app.post("/add")
def add_data(new_data: item):
    return new_data
