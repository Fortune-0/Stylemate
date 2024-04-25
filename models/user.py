#!/usr/bin/python3
"""User class for table containging user information"""

from models.base import Base
from sqlalchemy import String, Integer, Column

class User(Base):
    """Mapped User Class for user table"""

    __tablename__ = "user"
    name = Column(String(60), nullable=False, primary_key=True)
    age = Column(Integer, nullable=True)
    sex = Column(String(10), nullable=False)
