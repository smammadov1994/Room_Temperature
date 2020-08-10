try:
	from flask import Flask
	from flask_restful import Resource,Api
	from flask_restful import reqparse
	from flask import request
	from flask_httpauth import HTTPBasicAuth
	import time
	import datetime
	import json
	import Adafruit_DHT
	print("All modules loaded ")
except Exception as e:
	print("Error: {}".format(e))

app=Flask(__name__)
api=Api(app)
auth=HTTPBasicAuth()
pin = 17
sensor = Adafruit_DHT.DHT11

USER_DATA = {
    "admin":"admin"
}

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

class Temperature(Resource):
	def __init__(self):
		pass
		
	@auth.login_required 
	def get(self):
		print("checking temperature")
		humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
		if humidity is not None and temperature is not None:
			return(temperature*1.8+32)

api.add_resource(Temperature, "/")

if __name__ == "__main__":
	app.run(host='0.0.0.0')




