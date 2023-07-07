import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import Publisher, Book, Shop, Stock, Sale, create_tables

DSN = "postgresql://postgres:tgntityrj@localhost:5432/ORM_HW"
engine = sqlalchemy.create_engine(DSN)

if __name__ == '__main__':
    create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

pub1 = Publisher(name='Дрофа')
pub2 = Publisher(name='Росмэн')
pub3 = Publisher(name='Терра')
session.add_all([pub1, pub2, pub3])
session.commit()

shop1 = Shop(name='Лабиринт')
shop2 = Shop(name='Читай-Город')
shop3 = Shop(name='Буквоед')
session.add_all([shop1, shop2, shop3])
session.commit()

book1 = Book(title='Мастер и Маргарита', publisher=pub1)
book2 = Book(title='Унесенные ветром', publisher=pub2)
book3 = Book(title='Капитанская дочка', publisher=pub3)
session.add_all([book1, book2, book3])
session.commit()

st1 = Stock(book=book1, shop=shop1, count=132)
st2 = Stock(book=book1, shop=shop2, count=67)
st3 = Stock(book=book2, shop=shop1, count=39)
st4 = Stock(book=book2, shop=shop3, count=211)
st5 = Stock(book=book3, shop=shop2, count=52)
session.add_all([st1, st2, st3, st4, st5])
session.commit()

sale1 = Sale(price=2390, date_sale='20.03.2023', stock=st1, count=98)
sale2 = Sale(price=1950, date_sale='18.05.2023', stock=st2, count=114)
sale3 = Sale(price=2340, date_sale='12.05.2023', stock=st3, count=64)
sale4 = Sale(price=1200, date_sale='23.05.2023', stock=st4, count=48)
sale5 = Sale(price=2240, date_sale='28.05.2023', stock=st5, count=199)
session.add_all([sale1, sale2, sale3, sale4, sale5])
session.commit()


pub_search = input('Введите наименование издательства или id для поиска: ')

if pub_search.isnumeric():
    for c in session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.id == int(pub_search)).all():
        title_book, name_shop, c_price, c_data = c
        print(f'{title_book} | {name_shop} | {c_price} | {c_data}')
else:
    for c in session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.name.like(f'%{pub_search}%')).all():
        title_book, name_shop, c_price, c_data = c
        print(f'{title_book} | {name_shop} | {c_price} | {c_data}')
session.close()

