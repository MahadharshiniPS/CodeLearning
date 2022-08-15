from datetime import datetime
from pydantic import BaseModel

class Shopping_sch(BaseModel):
    username :str
    products_purchased : str
    total_cost :int
    date_of_purchase : datetime
