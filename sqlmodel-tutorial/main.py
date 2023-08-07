'''
Main.py
'''
from typing import Optional

from sqlmodel import Field, SQLModel, create_engine

class Hero(SQLModel, table=True):
    '''
    My Hero Docstring
    '''
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


SQLITE_FILE_NAME = "database.db"
SQLITE_DB = f"sqlite:///{SQLITE_FILE_NAME}"

engine = create_engine(SQLITE_DB, echo=True)

SQLModel.metadata.create_all(engine)
