import functions
import csv
from datetime import datetime


def main():
  while True:
      if functions.check_data():  
          data = functions.call_weather_api()
        
          # get time now
          nowUFC = datetime.now()
          nowUFC = str(nowUFC)
          hourEST = functions.time_convert(str(nowUFC))
                  
          # get user phone number
          phone_number = ''
          hot = 0
          cold = 0
          name = ''
          with open("info.csv", "r") as file:
              csv_reader = csv.reader(file)
              for row in csv_reader:
                  phone_number = row[3]
                  hot = int(row[1])
                  cold = int(row[2])
                  name = row[0]
                  break  
              
          weather_general = data["weather_general"]
          weather_more_descriptive = data["weather"]
          temperature_max = data['temperature_max']
          temperature_min = data['temperature_min']
          feels_like = data["feels_like"]
        
          arr_temp = ['hot', 'slightly cool', 'cold']
          arr_items = [
            'an umbrella', 'sunscreen', 'a wind-breaker', 'a pair of gloves',
            'a beanie', 'a scarf'
          ]
          arr_clothes = [
            'a T-shirt', 'a pair of shorts', 'a hoodie', 'a jacket',
            'a pair of trousers', 'multiple layers of clothing'
          ]
        
          while True:
            if nowUFC[11:13] == "10":
              #conditional statements — CHECKING TEMPERATURE
              if feels_like < cold:
                message1 = f"Today is {arr_temp[2]}. \
The temperature range is currently {temperature_min} Celsius - {temperature_max} Celsius. \
It feels like {feels_like} Celsius. \
Please don't forget to put on a {arr_clothes[5]}!"
        
              elif cold < feels_like < hot:
                message1 = f"Today is {arr_temp[1]}. \
The temperature is currently {temperature_min} Celsius - {temperature_max} Celsius. \
It feels like {feels_like} Celsius. \
Please don't forget to put on a {arr_clothes[2]} or {arr_clothes[3]}, as well as {arr_clothes[4]}!"
        
              else:
                message1 = f"Today is {arr_temp[0]}. \
The temperature is currently {temperature_min} Celsius - {temperature_max} Celsius. \
It feels like {feels_like} Celsius. \
Please don't forget to put on a {arr_clothes[0]} and {arr_clothes[1]}!"
        
              #conditional statements — CHECKING General Condition
              if weather_general == 'Rain' or weather_general == 'Drizzle' or weather_general == 'Thunderstorm':
                message2 = f"There will also be a {weather_more_descriptive}, so don't forget to bring {arr_items[0]}"
              elif weather_general == 'Snow':
                message2 = f"There will also be a {weather_more_descriptive}, so don't forget to bring {arr_items[3]}, {arr_items[4]}, and {arr_items[5]}"
              elif weather_general == 'Clouds' or 'Atmosphere':
                message2 = f"There will also be a {weather_more_descriptive}."
              functions.email_alert(f"Dear {name}",
                                    f"\n{message1} {message2}\nEnjoy your day!",
                                    f"{phone_number}@tmomail.net")
              break
          break
      else:
          data = functions.call_weather_api()
          user_info = functions.get_info()
          functions.save_data(data, user_info)


if __name__ == "__main__":
  main()

#T-mobile + Mint ending: ...@tmomail.net
#Spring ending: ...@messaging.sprintpcs.com
#Verizon ending: ...@vtext.com
#Virgin Mobile: ...@vmobl.com
#AT-T: ...@txt.att.net
#Boost Mobile: ...@sms.myboostmobile.com
