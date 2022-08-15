from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


sql_db_URL = 'sqlite:///./blog.db'

engine = create_engine(sql_db_URL,connect_args={"check_same_thread": False})

local_session = sessionmaker(bind=engine,autocommit=False, autoflush=False)

Base = declarative_base()