from pydantic import BaseModel

class Blog_sch(BaseModel):
    title : str
    body: str
