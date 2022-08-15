from venv import create
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db_URL = 'sqlite:///./shopping_cart.db'
engine = create_engine(db_URL,connect_args={"check_same_thread": False})

session = sessionmaker(bind=engine,autocommit=False, autoflush=False)

Base = declarative_base()