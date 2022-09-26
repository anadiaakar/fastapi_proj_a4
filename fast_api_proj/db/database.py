from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging
# sql_db_url = "postgresql://postgres:new_password@localhost:5432/fastapi";
sql_db_url = "postgresql://postgres:postgres@localhost:5432/fast_api"
engine = create_engine(sql_db_url,pool_size=20)

LSession = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()
# logging.basicConfig(filename='app.log', filemode='w+', format='%(asctime)s - %(levelname)s - %(message)s')
# logging.warning('This will get logged to a file')
# log = logging.getLogger(__name__)
