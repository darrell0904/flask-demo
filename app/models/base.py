'''
  Created By FJW in 20181021  
'''
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, SmallInteger

db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True
    # create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def set_attrs(self, attrs):
        for key, value in attrs.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)