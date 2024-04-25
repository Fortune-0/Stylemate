#!/usr/bin/python3
"""Create Base and parent class for Top and Bottom"""
from sqlalchemy import Column, Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class BaseItem():
    """Parent class for Top and Bottom"""

    id = Column(Integer, primary_key=True, default=0, nullable=False, autoincrement=True)
    name = Column(String(30), nullable=False)
    number = Column(Integer, nullable=False)
