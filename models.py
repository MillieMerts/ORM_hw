import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Publisher(Base):
    __tablename__ = "publishers"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=60), unique=True)

    def __str__(self):
        return f'{self.id}: {self.name}'

class Book(Base):
    __tablename__ ="books"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=120))
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publishers.id'))

    publisher = relationship(Publisher, backref='books')

class Shop(Base):
    __tablename__ = "shops"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40))

class Stock(Base):
    __tablename__ = 'stocks'

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('books.id'))
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shops.id'))
    count = sq.Column(sq.Integer)

    book = relationship(Book, backref='stocks')
    shop = relationship(Shop, backref='stocks')

class Sale(Base):
    __tablename__ = 'sales'

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer, nullable=False)
    date_sale = sq.Column(sq.Date, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stocks.id'))
    count = sq.Column(sq.Integer)

    stock = relationship(Stock, backref='sales')

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)