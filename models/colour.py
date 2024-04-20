#!/usr/bin/python3
"""Mapped Colour class for table of allowed colours"""

from models.base import Base
from sqlalchemy inport String
from sqlalchemy.orm import Column

class Colour(Base):
    """Colour table mapped class"""

    __tablename__ = "colours"
    name = Column(String(20), nullable=False, primary_key=True)
    hex_code = Column(String(7), nullable=True)
