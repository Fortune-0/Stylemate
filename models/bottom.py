#!/usr/bin/python3
"""Create 'bottom' table mapped class Bottom"""
from models.base import BaseItem
from models.base import Base

class Bottom(BaseItem, Base):
    """Bottom table mapped class"""

    __tablename__ = "bottoms"
