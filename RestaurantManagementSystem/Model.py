# make Restaurant database tables here...
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

databaseURL = "mysql+pymysql://Amrit:PariShubhangi24@localhost:3306/Restaurant"
engine = create_engine(databaseURL, echo=True)   # Connects to MySQL
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)   # Temporary interactive window to execute database actions
session = sessionLocal()
Base = declarative_base()

class admin(Base):
    __tablename__ = "Admin"
    identityNumber = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    discount = Column(Integer)

class staff(Base):
    __tablename__ = "Staff"
    identityNumber = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

class credentials(Base):
    __tablename__ = "Credentials"
    identityNumber = Column(Integer, ForeignKey('Admin.identityNumber'), primary_key=True)
    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)

class customers(Base):
    __tablename__ = "Customers"
    name = Column(String(100), nullable=False)
    mobileNumber = Column(String(100), primary_key=True)
    paymentMethod = Column(String(100), nullable=False)
    firstVisit = Column(String(100), nullable=False)
    currentVisit = Column(String(100), nullable=False)
    membershipCard = Column(Boolean, nullable=False)
    cardVisits = Column(Integer, nullable=False)

class membership_card(Base):
    __tablename__ = "MembershipCard"
    cardType = Column(Integer, primary_key=True, nullable=False)
    cardPrice = Column(Float, nullable=False)
    cardMaximumVisits = Column(Integer, nullable=False)
    discountAdded = Column(Integer, nullable=False)

class menu(Base):
    __tablename__ = "Menu"
    itemId = Column(Integer, primary_key=True, nullable=False)
    itemName = Column(String(100), unique=True, nullable=False)
    itemPrice = Column(Float, nullable=False)

class discounts(Base):
    __tablename__ = "Discounts"
    role = Column(String(100), nullable=False, primary_key=True)
    discount = Column(Integer, nullable=False)

# 2. Five tables: Admin [ID, Name, Discount], Staff [ID, Name], Menu [Item name, ID, Price], Credentials [ID, Name, Username, Password (Hashed)],
# 2 (cont'd). Customers [Name, Mobile Number, Payment Method, First Visit, Current Visit] (Customers table is optional)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Table created successfully")
