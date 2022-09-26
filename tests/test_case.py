from fastapi.testclient import TestClient
from sqlalchemy import create_engine 
from sqlalchemy_utils.functions.database import database_exists , create_database

import json
from fast_api_proj.db.database import Base , LSession
from fast_api_proj.main import app, get_db
import pytest

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/fast_api"


@pytest.fixture(scope="session")
def db_engine():
	engine = create_engine(SQLALCHEMY_DATABASE_URL)
	if not database_exists:
		create_database(engine.url)

	Base.metadata.create_all(bind=engine)
	yield engine


@pytest.fixture(scope="function")
def db(db_engine):
	connection = db_engine.connect()

	# begin a non-ORM transaction
	transaction = connection.begin()

	# bind an individual Session to the connection
	db = LSession(bind=connection)
	

	yield db

	db.rollback()
	connection.close()


# 
@pytest.fixture(scope="function")
def client(db):
	
	app.dependency_overrides[get_db] = lambda: db

	with TestClient(app) as c:
		yield c


def test_api1(client):
	
	
	##API 1
	call = client.get('/emp/')
	assert call.status_code == 200

def test_api2_case_1(client):
	##API 2 CASE 1
	
	input_data = {'name':'ANadi Dewan Dewan', 'email':'ddSddaakaranadia@gmail.com', 'location':'Pune'}
	call = client.post('/emp/',data=json.dumps(input_data))
	print(call.text)
	assert call.status_code == 200

def test_api2_case_2(client):
	#API2 Case 2 incorrect input
	
	input_data = {'name':'Dewan', 'email':'sasa', 'location':'Pune'}
	call = client.post('/emp/',data=json.dumps(input_data))
	assert call.status_code == 422
	
def test_api2_case_3(client):
	#API2 Case 3 id exists
	
	input_data = {'name':'Dewan', 'email':'anadiaakar@gmail.com', 'location':'Pune'}
	call = client.post('/emp/',data=json.dumps(input_data))
	assert call.status_code == 400

def test_api3_case_1(client):
	
	#Case 1 correct id
	call = client.get('/details/2')
	assert call.status_code == 200

def test_api3_case_2(client):
	#Case 2 incorrect id
	
	call = client.get('/details/999999')
	assert call.status_code == 404

def test_api4_case_1(client):
	
	#Case1 correct id 
	input_data = {'name':'Dewan', 'email':'saxasa@gmail.com', 'location':'Pune'}
	call = client.patch('/emp_update/2',data=json.dumps(input_data))
	print(call.status_code)
	print(call.text)
	assert call.status_code == 200

def test_api4_case_2(client):
	#Case 2 incorrect id
	
	input_data = {'name':'Dewan', 'email':'sasa@gmail.com', 'location':'Pune'}
	call = client.patch('/emp_update/9999',data=json.dumps(input_data))
	assert call.status_code == 404
