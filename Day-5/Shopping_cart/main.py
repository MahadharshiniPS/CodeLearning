from fastapi import FastAPI,Depends,status,Response,HTTPException
import models
from models import Shopping
from sqlalchemy.orm import Session
from database_db import engine,session
from schemas import Shopping_sch


app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.get("/getall/items")
def get_shopping_items(db: Session = Depends(get_db)):
    get_data = db.query(Shopping_sch).all()
    return get_data


@app.get("/getbyid/{id}")
def get_by_id(id,db: Session = Depends(get_db)):
    get_by_id = db.query(Shopping).filter(Shopping.id == id).first()
    if not get_by_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail =f"Shopping cart with id {id} not found")
    return get_by_id


@app.post("/create",status_code=201)
def add_data(request :Shopping_sch,db: Session = Depends(get_db)):
    new_data = Shopping(username = request.username,products_purchased= request.products_purchased,
          total_cost=request.total_cost,date_of_purchase=request.date_of_purchase)
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

@app.put("/edit/{id}",status_code=201)
def edit(id,request :Shopping_sch,db: Session = Depends(get_db)):
    edit = db.query(Shopping).filter(Shopping.id == id)
    if not edit.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"Shopping cart with id {id} not found,hence cannot update")
    edit.update(request)
    db.commit()
    return {'detail': f'Shopping cart with id {id} updated successfully'}


@app.delete("/delete/{username}")
def delete_data(username,db: Session = Depends(get_db)):
    delete = db.query(Shopping).filter(Shopping.username == username)
    if not delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"Blog with id {id} not found,hence cannot delete")
    delete.delete(synchronize_session=False)
    db.commit()
    return {'detail': f'Shopping cart with id {username} deleted successfully'}