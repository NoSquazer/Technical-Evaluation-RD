# SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config import settings


engine = create_engine(settings.DB_URL)

Base = declarative_base()


class Database(Base):
    __tablename__ = "database"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    field_1 = Column(String)
    author = Column(String)
    description = Column(String)
    my_numeric_field = Column(String)


Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
