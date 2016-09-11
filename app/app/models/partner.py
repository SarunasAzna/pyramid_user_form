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
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    category_ids = relationship('Category', secondary=PartnerCategory,
                                backref='Partner')


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    partner_ids = relationship('Partner', secondary=PartnerCategory,
                               backref='Category')
