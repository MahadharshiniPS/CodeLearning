from database_db import Base 
from sqlalchemy import Column,Integer,String,Date

class Shopping(Base):
    __tablename__ = "Shopping_cart"

    id = Column(Integer,primary_key=True,index = True)
    username = Column(String)
    products_purchased = Column(String)
    total_cost = Column(Integer)
    date_of_purchase = Column(Date)