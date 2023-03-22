import sys

from db.config import get_config, get_connection_dsn
from db.db_model import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError

from utils import console

try:
    db = create_engine(get_connection_dsn(get_config()), echo=True)
    Base.metadata.create_all(db)
    SESSION = Session(db)
except OperationalError:
    console.print("Нет связи с БД!\n:no_entry_sign:", style="bold red")
    sys.exit()
