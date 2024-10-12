"""
Module migrations
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE

Base = declarative_base()


class User(Base):
    """
    Class User
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(255))
    account_type = Column(String(50), unique=False, index=True)
    role = Column(String(50), unique=False, index=True)


class Post(Base):
    """
    Class Post
    """
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    content = Column(String(50))
    user_id = Column(Integer)


# Configurar la base de datos
DATABASE_URL = (f"mysql+pymysql://{DATABASE['user']}:{DATABASE['password']}@"
                f"{DATABASE['host']}/{DATABASE['name']}")
engine = create_engine(DATABASE_URL)


# Crear una sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
