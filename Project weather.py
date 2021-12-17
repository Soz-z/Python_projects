# Zip code or city name
# Create function to check for zip code or city name.
# https://www.w3schools.com/python/python_try_except.asp?
#https://openweathermap.org/forecast5#5days
import requests
import json
import time

def input_check(user_input):
	#Checks if input is zipcode using .isdigit() https://www.w3schools.com/python/ref_string_isdigit.asp
	if user_input.isdigit() == True:
		#Checks the length of zipcode to ensure it is correct, if so returns zipcode
		run = True
		try:
			zipcode = int(user_input)
			if len(user_input) == 5:
				#Using 1 as check for formatting api request later.
				run = False
				return zipcode, 1
			else:
				print("Invalid Zipcode")
				print("Zipcode must be 5 digits long")
				zipcode = int(input("Enter Zipcode, only 5 digits: "))
				return zipcode, 1
					
		except:
			print("Error with zipcode format")
			exit()
	else:
		#A check for the inputted string will be done when the API request is done
		return user_input, 0

def welcome_message():
	print("Welcome to the Weather Program")
	time.sleep(1)
	print("This program will return a 12hr and 24hr weather forecast.")
	time.sleep(1)




def user_input_actual():
	user_input = input("Enter a zipcode or Location to check weather forecast: \n ")
	return user_input

def webservice(location, value):
	#https://nominatim.org/release-docs/develop/api/Search/
	#Using value to define an API request to either quiery a postal code or a city
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
    time.sleep(1)
    print("Gathering weather data")
    time.sleep(1)
    try:
        weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=imperial&cnt=9&appid={api}').text
        return weather_data
    except:
        print("Gathering Unsuccessful")

def weather_sort(data):
#Not really a sorter, just a function to help me control variables and data coming out of the API request
    for x in data:
        city = data['city']
        raw_data = data['list']
    for i in city:
        name = city['name']
        dt_sunrise = city['sunrise']
        dt_sunset = city['sunset']
    #https://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date
    #sunrise = time.ctime(int(dt_sunrise))
    #sunset = time.ctime(int(dt_sunset))
    sunrise = time.strftime("%H:%M", time.localtime(int(dt_sunrise)))
    sunset = time.strftime("%H:%M", time.localtime(int(dt_sunset)))
    twelve_hour = raw_data[3]
    twenty_four_hour = raw_data[7]
    return raw_data, name, sunrise, sunset, twelve_hour, twenty_four_hour


def weather_display(data):
#Taking a single indexed raw data and displaying it to the user.
    weather = data['weather']
    weather_main = weather[0]['main']
    description = weather[0]['description']
    main = data['main']
    temp = main['temp']
    feels_like = main['feels_like']
    humidity = str(main['humidity']) + '%'
    winds = data['wind']
    wind_speed = winds['speed']
    wind_gust = winds['gust']
    wind_dir = winds['deg']
    forecast_time = data['dt_txt'] + ' UTC'
    print(f'{forecast_time}    {description}\nTemperature: {temp}F   Feels like: {feels_like}F    Humidity: {humidity}')
    print(f'Wind speed at {wind_speed} MPH     gusting to {wind_gust} MPH     from {wind_dir} degrees')

def more_forecasts(name, raw_data):
#When doing this project I ended up using it for my own forecasts so I decided to add in this function so I could look at different time periods
        user_input = input(f"\nWould you like a forecast for different time in {name}? (y or n?) ")
        if user_input == 'y':
                print("Please select the forecast you want")
                print("1. 3 Hour \n2. 6 Hour \n3. 9 Hour \n4. 12 Hour \n5. 15 Hour \n6. 18 Hour \n7. 24 Hour")
                run = True
                #Using a "While True" to keep it in a loop rather than re-calling the function
                while run == True:
                        try:
                                new_input = input()
                                if new_input.isdigit() == True:
                                        number = int(new_input)
                                        if number >= 1 and number <7:
                                                 number = number - 1
                                                 weather_display(raw_data[number])
                                                 run = False
                                        else:
                                                print("input a number between 1 and 7")
                                                continue
                                else:
                                        print("Value must be an integer only.")
                                        continue
                        except: print("Program encountered an unknown error try again.")
        elif user_input == 'n':
                pass
        else:
                print("Wrong input, please use 'y' or 'n'"), more_forecasts(name, raw_data)

def startover():
	user_input = input('Would you like to get another forecast of a different location? (y or n) ')
	if user_input == 'y':
		main()
		#Would like to take out the welcome function without having to build a new Main() so the user doesn't have to see it.
	elif user_input == 'n':
		print("Thank you for using the Weather Program!")
		leave = input("Press enter to leave...")
	else:
		print(f'Does {user_input} look like a "y" or "n"? I did not think so.')
		print('Nice try, trying to break me. Good-bye....')
		leave = input("Press enter to leave...")
                

def main():
	welcome_message()
	user_input = input("Please input a Zipcode or City: ")
	unchecked_input = (user_input)
	location, value = input_check(unchecked_input)
	lat, lon = webservice(location, value)
	api = "52df91efe3d8aead183175f99f2568e8"
	weather_json = weather_service(lat, lon, api)
	api_pull = json.loads(weather_json)
	raw_data, name, sunrise, sunset, twelve_hour, twenty_four_hour = weather_sort(api_pull)
	print()
	print(name)
	print()
	print("12 Hour Forecast (data updated every 3 hours)")
	weather_display(twelve_hour)
	print("\n24 Hour Forecast")
	weather_display(twenty_four_hour)
	more_forecasts(name, raw_data)
	startover()
	
main()

