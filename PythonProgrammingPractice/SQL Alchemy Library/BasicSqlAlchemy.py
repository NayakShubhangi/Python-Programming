# SQL Alchemy is a powerful ORM (Object Relational Mapper) for interacting with databases using Python objects instead of raw SQL queries.

# Steps:
# 1. Install dependencies
# 2. Conenct Python to MYSQL
# 3. Define database models (models = tables)
# 4. Create tables in database

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

databaseURL = "mysql+pymysql://Amrit:PariShubhangi24@localhost:3306/python_practice"
engine = create_engine(databaseURL, echo=True)   # Connects to MySQL
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)   # Temporary interactive window to execute database actions
Base = declarative_base()

class clsTwo(Base):   # Only this class will be considered by Python to create tables
    # __tablename__ = "EmployeeInfo"
    # emp_id = Column(Integer, primary_key=True, autoincrement=True)
    # emp_first_name = Column(String(100), nullable=False)
    # emp_first_name = Column(String(100), nullable=False)
    # emp_job = Column(String(100), nullable=False)
    # emp_department = Column(String(100), nullable=False)
    __tablename__ = "CustomerOrderInfo"
    order_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String(100), nullable=False)
    product_name = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
# Don't need to comment out; SQL Alchemy checks whether a table with the tablename already exists. If there is an existing table with that name,
# it won't create the table. If a table with that name doesn't exist, only then will it create that table.

Base.metadata.create_all(bind=engine)   # Binds the engine to the session and creates all tables that have inherited Base
print("Table created successfully")

# clsTwoObj = clsTwo(id=424919, name="Shubhangi")
# sessionLocal().add_all([clsTwoObj])
# sessionLocal().commit()
# fetchData = sessionLocal().query(clsTwo).all()

# for i in fetchData:
#     print(i.TableTwo_id)
#     print(i.TableTwo_name)
#     print("this is for loop")



# TASK ONE:
# Create two tables in a single program, and verify their existence by using the mysql command line (use python_practice, show tables;)
# Each table should have at least 5 columns with different datatypes (Integer, String, ect..)
# just empty columns is fine

# NOTE: Created tables employeeinfo and customerorderinfo

# TASK TWO:
# Go through Flask, Django, and FastAPI. Compare the three.
# Flask: A web framework that allows you to build web applications.
# Django: A web framework that allows you to build web applications.
# FastAPI: A web framework that allows you to build web applications.

# Differences:
# Flask is a microframework which only has tools that are important, making it flexible and suitable for smaller applications.
# Django is a full-stack framwork which has a lot of built-in features, making it suitable for bigger applications. However, it is less flexible.
# FastAPI is a high-performance framework designed to build APIs, and it is suitable for fast, high-performing applications and API building.

# TASK THREE:
# Go through data classes again. (Data_classes.py)

# TASK FOUR (continued):
# Go through callable built-in function, breakpoint function, complex, isinstance, compile.
# Callable: Checks if an object is callable
# Breakpoint: Used to enter interactive debugging mode
# Complex: Creates a complex number
# Isinstance: Checks if an object is an instance of a specified class or type
# Compile: Compiles the code