from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(50), unique=True, required=True)
    password = Column(String(50))
    role = Column(String(20))

class Picker(Base):
    __tablename__ = 'pickers'

    id = Column(Integer, primary_key=True)
    name= Column(String(50))
    phone_number = Column(String(15),required=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name= Column(String(50))
    phone_number = Column(String(15))
    account_id = Column(Integer, ForeignKey('accounts.id'))
