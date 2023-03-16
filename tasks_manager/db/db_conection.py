from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.settings import db_user, db_pass, db_host, db_port, db_name

db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)

session = Session(db)
