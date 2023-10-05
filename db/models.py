from .database import Base
import sqlalchemy

class Employee(Base):
	__tablename__ = "Employee"

	id = sqlalchemy.Column(sqlalchemy.Integer , primary_key = True , index=True)
	name = sqlalchemy.Column(sqlalchemy.String)
	email = sqlalchemy.Column(sqlalchemy.String , unique=True, index=True)
	location = sqlalchemy.Column(sqlalchemy.String)
	is_active= sqlalchemy.Column(sqlalchemy.Boolean, default = True)
	password = sqlalchemy.Column(sqlalchemy.String)
	contact = sqlalchemy.Column(sqlalchemy.String)


class Company(Base):
	__tablename__ = "Company"

	id = sqlalchemy.Column(sqlalchemy.Integer , primary_key = True , index=True)
	name = sqlalchemy.Column(sqlalchemy.String)
	location = sqlalchemy.Column(sqlalchemy.String)
	is_active= sqlalchemy.Column(sqlalchemy.Boolean, default = True)
	contact = sqlalchemy.Column(sqlalchemy.String)
	active_products = sqlalchemy.Column(sqlalchemy.String)
	inactive_products = sqlalchemy.Column(sqlalchemy.String)

