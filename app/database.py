from .models.base import Base
from .engine import engine

def init_db():
    Base.metadata.create_all(bind=engine) 