#!/usr/bin/python3
"""Create 'top' table mapped class Top"""
from models.base import BaseItem
from models.base import Base

class Top(BaseItem, Base):
    """Top table mapped class"""

    __tablename__ = "tops"
