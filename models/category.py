#!/usr/bin/python3
"""Category table for type of clothing item"""

from models.base import Base
from sqlalchemy import Column, String

class Category(Base):
    """Category class"""

    __tablename__ = "categories"
    name = Column(String(20))
