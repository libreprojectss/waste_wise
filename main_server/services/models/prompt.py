from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from datetime import datetime

Base = declarative_base()
class PromptData(Base):
    __tablename__ = "prompt_data"

    id = Column(Integer, primary_key=True, index=True)
    request_key = Column(String, index=True)
    request_type = Column(String)
    result = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

