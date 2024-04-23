#!/usr/bin/python3
"""Create Base and parent class for Top and Bottom"""
from sqlalchemy import Column, Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base
import models
import uuid

Base = declarative_base()

class BaseItem(Base):
    """Parent class for Top and Bottom"""

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    category = Column(ForeignKey("category.name"), nullable=False)
    number = Column(Integer, nullable=False)
    
    def save(self):
        """Update the attribute with the current date and time"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()
        
    def delete(self):
        """Delete the instance from storage"""
        models.storage.delete(self)