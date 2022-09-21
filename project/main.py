
from fastapi import FastAPI , Depends , HTTPException
from sqlalchemy.orm import Session
import uvicorn
from db import crud, models , schema
from db.database import LSession , engine 
from typing import List
# from db.crud import logger

app = FastAPI()

def get_db():
	db = LSession()
	crud.logger.info('Creating Session')
	try:
		yield db
	finally:
		# db.commit()
		crud.logger.info('Closing Session')
		db.close()

@app.get("/emp/",response_model=List[schema.Employee])
def view(skip : int = 0 , limit : int=100 , db : Session = Depends(get_db)):
	crud.logger.info('View called for emp list')
	emp = crud.get_users(db , skip=skip, limit= limit)
	return emp

@app.post("/emp/", response_model = schema.EmployeeCreate)
def create_user(Employee : schema.EmployeeCreate , db: Session = Depends(get_db)):
	if '@' not in Employee.email and "." not in Employee.email:
		raise HTTPException(status_code=422, detail="Unprocessable entity")
	db_user = crud.get_user_by_email(db , email= Employee.email)
	if db_user:
		raise HTTPException(status_code=400, detail="Email already registered")
	return crud.create_employee(db=db, user=Employee)

@app.get("/details/{user_id}", response_model = schema.Employee)
def read_user(user_id : int , db : Session = Depends(get_db)):
	db_user = crud.get_user(db,employee_id=user_id)
	if db_user is None:
		raise HTTPException(status_code=404, detail="User not found")
	return db_user

@app.patch("/emp_update/{emp_id}", response_model = schema.Employee)
def update_user(emp_id : int ,emp : schema.EmployeeUpdate,db : Session = Depends(get_db) ):
	db_user = crud.get_user(db,employee_id=emp_id)
	if db_user is None:
		raise HTTPException(status_code=404, detail="User not found")
	return crud.update_employee(db , emp_id=emp_id ,emp = emp)

if __name__ == "__main__":

	uvicorn.run(app,host="127.0.0.1",port=8000)
