from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Website(Base):
    __tablename__ = "websites"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    url = Column(String(255))
    status = Column(String(50))

class PiHoleData(Base):
    __tablename__ = "pihole_data"
    id = Column(Integer, primary_key=True, index=True)
    metric = Column(String(255))
    value = Column(Integer)

class TrainSchedule(Base):
    __tablename__ = "train_schedule"
    id = Column(Integer, primary_key=True, index=True)
    route = Column(String(255))
    next_train_time = Column(String(50))

class PublicTrash(Base):
    __tablename__ = "public_trash"
    id = Column(Integer, primary_key=True, index=True)
    location = Column(String(255))
    hours = Column(String(50))

Base.metadata.create_all(bind=engine)
