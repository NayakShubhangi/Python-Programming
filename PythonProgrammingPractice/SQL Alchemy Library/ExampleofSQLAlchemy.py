from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from BasicSqlAlchemy import clsTwo

databaseURL = "mysql+pymysql://Amrit:PariShubhangi24@localhost:3306/python_practice"
engine = create_engine(databaseURL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
# How to insert data into table:
# user = clsTwo(order_id=12345, customer_name="Bob", product_name="Cookies", quantity=1000, price=399.99)
# session.add(user)
# session.commit()
# How to fetch data from table:
users = session.query(clsTwo).all()
print(type(users[0]))
for user in users:
    print(f"{user.order_id}")
    print(f"{user.customer_name}")
    print(f"{user.product_name}")
    print(f"{user.quantity}")
    print(f"{user.price}")