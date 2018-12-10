path.append(getcwd() + "/dao")
import SchorrDAO
import json

class SchorrService:
	def __init__():

	def query_database(self, dictionary):


	def get_headers(self):
		response = False
		try:
			response = SchorrDAO().get_headers()
		except:
			response = False

		return response