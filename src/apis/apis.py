from flask import Flask, request
from sys import path
from os import getcwd
path.append(getcwd() + "/service")
import SchorrService
import json

app = Flask(__name__)

#This just allows other servers to hit our APIs
@app.after_request
def add_header(response):
	response.headers['Access-Control-Allow-Origin'] = '*'
	return response

#Takes the database, username, and password in a JSON, parese it and sets it so we can make changes.
#If the change is successful, True is returned.
#If the change is unsuccessfull for any reason, False is returned.
#@app.route('/set_database', methods=['POST'])
#def set_database():
#	dictionary = json.loads(request.get_json(force=True))
#	response = False
#	try{
#		response = SchorrService().set_database(dictionary['database'], dictionary['username'], dictionary['password'])
#	}except{
#		response = False
#	}
#	return response

#Takes the a query consisting of a JSON object with the table key and a value and query's the database on it.
#On success, it will return a list of JSON objects.
#On failure, it will reutrn an empty list
@app.route('/query', methods=['POST'])
def query_data():
	dictionary = json.loads(request.get_json(force=True))
	response = []
	try:
		response = SchorrService().query_database(dictionary)
	except:
		response = []
	
	return response

#Takes a JSON containg the table name and fields and adds them to the database as a new table
#Returns True if successful
#Returns False if unsuccessful
#@app.route('/add_table', methods=['POST'])
#def add_table():
#	json = request.get_json(force=True)
#	response = False
#	try{
#		response = SchorrService().add_table(json)
#	}except{
#		response = False
#	}
#	return response

#Takes a JSON containing a table name and field data and adds it to the database as a new row
#Returns True if successful
#Returns False if unsuccessful
#@app.route('/add_row', methods=['POST'])
#def add_row():
#	dictionary = json.loads(request.get_json(force=True))
#	response = False
#	try:
#		response = SchorrService().add_table(dictionary)
#	except:
#		response = False
	

#	return response

#Takes a table rowID and a table name and deletes that row from that table
#Returns True if successful
#Returns False if unsuccessful
#@app.route('/delete_row', methods=['POST'])
#def delete_row():
#	dictionary = json.loads(request.get_json(force=True))
#	response = False
#	try:
#		response = SchorrService().delete_row(dictionary['tableName'], dictionary['rowId'])
#	except:
#		response = False
#	
#	return response

#Takes a table name and deletes it from that database
#Returns True if successful
#Returns False if unsuccessful
#@app.route('/delete_table', methods=['POST'])
#def delete_table():
#	dictionary = json.loads(request.get_json(force=True))
#	response = False
#	try{
#		response = SchorrService().delete_table(dictionary['tableName'])
#	}except{
#		response = False
#	}
#	return response

#Takes a JSON containing a tableName and returns all the headers for that table
#Returns True if successful
#Returns False if unsuccessful
@app.route('/get_headers')
def get_headers():
	response = False
	try:
		response = SchorrService().get_headers()
	except:
		response = False
	
	return response
























