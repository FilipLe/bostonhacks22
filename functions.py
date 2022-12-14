import sys
import requests
import smtplib
from email.message import EmailMessage
import csv
'''
Time converter function
'''

def boston_time_api_convert(time):
  if "15" in time:
    return time[0:11] + "10" + time[13:]
  elif "18" in time:
    return time[0:11] + "13" + time[13:]
  elif "21" in time:
    return time[0:11] + "16" + time[13:]
  else:
    return time[0:11] + "19" + time[13:]


'''
Time formatting
'''


def time_convert(s):
  hour = (int(s[11:13]) + 19) % 24
  if hour < 10:
    hour = "0" + str(hour)
  else:
    hour = str(hour)
  return hour


'''
Collect info
'''


def get_info():
  name = input("Hi! Welcome to your Automatic Wardrobe, what’s your name? ")
  print(f"Hi {name} ! At what temperature do you think fits these categories?")
  hot = input("When does it start to feel hot? ")
  cold = input("When does it start to feel cold? ")
  phone_number = input(
    "Cool! Can we get your number by the way?( ͡° ͜ʖ ͡°) : ")
  print(
    f"Alright {name}, we will send you a notification about the weather every morning at 8am, smell ya later!"
  )

  return {"name": name, "hot": hot, "cold": cold, "phone_number": phone_number}


'''
SMS messaging function
'''


def email_alert(subject, body, to):
  msg = EmailMessage()
  msg.set_content(body)
  msg['subject'] = subject
  msg['to'] = to

  account = "filipclashroyale2004@gmail.com"
  msg['from'] = account
  #this passcode is generated by Google's 2 Factory Authorization in Security section of Account
  password = "xwctfykoxnlgskbm"

  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login(account, password)
  server.send_message(msg)

  server.quit()


'''
Call weather API function
'''


def call_weather_api():
  API_KEY = "1995efd78faaa85192e41d05356ff5bf"
  BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

  city = "Boston"
  request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
  response = requests.get(request_url)
  '''
  Collecting and handling weather information 
  '''
  if response.status_code == 200:
    #import the collected data
    data = response.json()

    #general category - e.g., clouds
    weather_general = data["list"][0]['weather'][0]['main']

    #more descriptive - e.g., few clouds, scattered clouds, etc.
    weather = data["list"][0]['weather'][0]['description']

    #current time
    time = data["list"][0]["dt_txt"]

    #max temperature of the day in Celsius
    temperature_max = round(data["list"][0]["main"]["temp_max"] - 273.15, 2)

    #min temperature of the day in Celsius
    temperature_min = round(data["list"][0]["main"]["temp_min"] - 273.15, 2)
    #feels like in Celsius
    feels_like = round(data["list"][0]["main"]["feels_like"] - 273.15, 2)
    #wind speed
    wind_speed = data["list"][0]["wind"]["speed"]

    #list[1] weather afternoon
    feels_like_afternoon = round(
      data["list"][1]["main"]["feels_like"] - 273.15, 2)

    #list[2] weather at night
    feels_like_night = round(data["list"][2]["main"]["feels_like"] - 273.15, 2)

    return {
      "weather_general": weather_general,
      "weather": weather,
      "time": time,
      "temperature_min": temperature_min,
      "temperature_max": temperature_max,
      "feels_like": feels_like,
      "wind_speed": wind_speed,
      "feels_like_afternoon": feels_like_afternoon,
      "feels_like_night": feels_like_night
    }

  else:
    print("An error occurred.")
    sys.exit()

def check_data():
    try:
        file = open("info.csv", 'r')
        file.close()
        return True
    except:
        return False

def save_data(data, user_info):
    p = [user_info["name"], user_info["hot"], user_info["cold"], user_info["phone_number"]\
        ,data["weather_general"], data["weather"], data["time"], data["temperature_min"] \
        ,data["temperature_max"], data["feels_like"], data["wind_speed"]]
    
    with open("info.csv", "w") as file:
        write = csv.writer(file)
        write.writerow(p)
