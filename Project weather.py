# Zip code or city name
# Create function to check for zip code or city name.
# https://www.w3schools.com/python/python_try_except.asp?
import requests
import json
import time


# Change to user input later
# user_input = input("Enter a zipcode or Location to check weather forecast: \n ")
user_input = "76018"


def input_check(user_input):
	#Checks if input is zipcode using .isdigit() https://www.w3schools.com/python/ref_string_isdigit.asp
	if user_input.isdigit() == True:
		#Checks the length of zipcode to ensure it is correct, if so returns zipcode
		try:
			zipcode = int(user_input)
			if len(user_input) == 5:
				#Using 1 as check for formatting api request later.
				return zipcode, 1
			else:
				print("Invalid Zipcode")
		except:
			print("Error with zipcode format")
	else:
		return user_input, 0

def welcome_message():
	print("Welcome to the Weather Program")
	time.sleep(2)
	print("This program will return a weather forecast.")
	time.sleep(2)




def user_input_actual():
	user_input = input("Enter a zipcode or Location to check weather forecast: \n ")
	return user_input

def webservice(location, value):
	#https://nominatim.org/release-docs/develop/api/Search/
	print("Now trying to connect....")
	try:
		if value == 1:
            #https://docs.python.org/3/library/json.html
			json_data = requests.get(f'https://nominatim.openstreetmap.org/search?postalcode={location}&countrycodes=us&format=json&limit=1')
			data = json.loads(json_data.content)
		else:
			json_data = requests.get(f'https://nominatim.openstreetmap.org/search?city={location}&countrycodes=us&format=json&limit=1')
			data = json.loads(json_data.content)
			if len(data) == 0:
				#insert startover function
				print("Invalid City name or no results returned.")
				print("Would you like to try again? y or n")
				retry = input()
				if retry == 'y' or retry == 'Y':
					main()
				else: exit()

		for i in data:
			lat = i['lat']
			lon = i['lon']
		return lat, lon
	except:
		print("Unable to connect to webservice")
		#insert startover function
		print("Would you like to try again? y or n")
		retry = input()
		if retry == 'y' or retry == 'Y':
			main()
		else: exit()

def weather_service(lat, lon, api):
    print("Connection Successful.")
    time.sleep(2)
    print("Gathering weather data")
    #print("Would you like to exlude any of the following data?\ncurrent\nminutely\nhourly\ndaily\nalerts")
    try:
        weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API}')
        pass
    except:
        pass

def forecast_format(weather_unformatted):
	pass

def weather_display(weather_formatted):
	pass

def startover():
	pass

def main():
	welcome_message()
	# when finished change below to: unchecked_input = (user_input_actual)
	unchecked_input = (user_input)
	location, value = input_check(unchecked_input)
	lat, lon = webservice(location, value)
	api = "52df91efe3d8aead183175f99f2568e8"
	weather_unformatted = weather_service(lat, lon, api)

main()
