from fastapi import FastAPI,Depends,status,Response,HTTPException
from schemas import Blog_sch
import models 
from models import Blog
from sqlalchemy.orm import Session
from database import engine,local_session
app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()


@app.get('/all/blog')
def get_all_blogs(db: Session = Depends(get_db)):
    get_blog = db.query(Blog).all()
    return get_blog


@app.get('/blog/{id}')
def get_all_blogs(id : int,db: Session = Depends(get_db)):
    get_blog = db.query(Blog).filter(Blog.id == id).first()
    if not get_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail =f"Blog with id {id} not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
    return get_blog


@app.post("/blog",status_code=201)
def create_blog(request:Blog_sch,db: Session = Depends(get_db)):
    new_blog = Blog(title = request.title,body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.put("/update/blog/{id}")
def update_blog_by_id(id,request :Blog_sch,db: Session = Depends(get_db)):
    updated = db.query(Blog).filter(Blog.id == id)
    if not updated.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"Blog with id {id} not found,hence cannot update")
    updated.update(request.dict())
    db.commit()
    return {'detail':f'Blog with id {id} updated successfully'}



@app.delete("/blog/delete/{id}")
def delete_blog(id,db: Session = Depends(get_db)):
    delete_blog = db.query(Blog).filter(Blog.id == id)
    if not delete_blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"Blog with id {id} not found,hence cannot delete")
    
    delete_blog.delete(synchronize_session=False)
    db.commit()
    return {'detail':f'Blog with id {id} deleted successfully'}

