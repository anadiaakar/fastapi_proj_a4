from sqlalchemy.orm import Session

from . import models , schema 

import logging
from logging.config import dictConfig
from db.schema import LogConfig
from sqlalchemy.dialects import postgresql

dictConfig(LogConfig().dict())
logger = logging.getLogger("mycoolapp")




def get_user(db: Session , employee_id : int):
	quer = db.query(models.Employee).filter(models.Employee.id == employee_id)
	logger.info('query '+ str(quer.statement.compile(dialect=postgresql.dialect())))
	return quer.first()

def get_user_by_email(db: Session , email : str):
	quer = db.query(models.Employee).filter(models.Employee.email==email)
	logger.info('query '+ str(quer.statement.compile(dialect=postgresql.dialect())))
	return quer.first()


def update_employee(db:Session , emp_id: int ,emp: schema.EmployeeUpdate):
	logger.info('Updating Employee')
	db_employee = get_user(db,emp_id)
	if db_employee:
		logger.info(str(db_employee.id)+ 'User Found!')
	else:
		logger.info('User Not Found!')
	emp_data = emp.dict(exclude_unset=True)
	for key , value in emp_data.items():
		setattr(db_employee,key,value)
	db.commit()
	db.refresh(db_employee)
	return db_employee

def get_users(db: Session , skip : int = 0, limit: int=100):
	quer = db.query(models.Employee).offset(skip).limit(limit)
	logger.info('query '+ str(quer.statement.compile(dialect=postgresql.dialect())))
	return quer.all()

def create_employee(db: Session , user : schema.EmployeeCreate):
	logger.info('Creating Employee')
	logger.info(str([user.email , user.location , user.name ]))
	db_user = models.Employee(email=user.email , location=user.location , name = user.name)
	db.add(db_user)
	print(user.dict())
	db.commit()
	db.refresh(db_user)
	return user






