from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .meta import Base


PartnerCategory = Table(
    'PartnerCategory',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('partnerId', Integer, ForeignKey('partner.id')),
    Column('categoryId', Integer, ForeignKey('category.id'))
)


class Partner(Base):
    __tablename__ = 'partner'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    category_ids = relationship('Category', secondary=PartnerCategory,
                                backref='Partner')


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    partner_ids = relationship('Partner', secondary=PartnerCategory,
                               backref='Category')



#Index('my_index', MyModel.name, unique=True, mysql_length=255)
