import os

from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv


load_dotenv()
PASSWORD = os.getenv("MYSQL_PASSWORD") 

engine = create_engine(f"mysql+pymysql://root:{PASSWORD}@localhost:3306/storedb")

meta = MetaData()

conn = engine.connect()