import requests

class City:
    def __init__(self, name, lat, lon, units="imperial"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=5123e95a7f509b0e9a4b2c571fa99c1f")

        except:
            print("No internet access :(")

        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]

    def temp_print(self):
        units_symbol = "C"
        if self.units == "imperial":
            units_symbol = "F"
        print(f"In Tampa it is currently {self.temp}° {units_symbol}")
        print(f"Today's High: {self.temp_max}° {units_symbol}")
        print(f"Today's Low: {self.temp_min}° {units_symbol}")

my_city = City("Tampa", 27.9641, -82.4526)
my_city.temp_print()

vacation_city = City("Orlando", 28.5384, -81.3789, units="imperial")
vacation_city.temp_print()
print(vacation_city.response_json)

