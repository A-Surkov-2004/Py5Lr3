
import json



def get_weather_data(place, api_key):
    import requests
    s = f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}'
    print(s);
    response = requests.get(s)
    res_obj = json.loads(response.text)
    ans = extract(res_obj)
    return ans
    
    
def extract(res_obj):
    ans = json.dumps({"name":res_obj["name"], "coord":res_obj["coord"], "country":res_obj["sys"]["country"],"feels_like (C)":round(res_obj["main"]["feels_like"]-273.15,2), "timezone":res_obj["timezone"]/60/60}, separators=(',', ':'))
    print(ans)
    return ans



if __name__ == "__main__":
    #decode()

    st = """{"coord": {"lon": 28.3496, "lat": 57.8136},
     "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}], "base": "stations",
     "main": {"temp": 291.1, "feels_like": 290.83, "temp_min": 291.1, "temp_max": 291.1, "pressure": 1031,
              "humidity": 72, "sea_level": 1031, "grnd_level": 1025}, "visibility": 10000,
     "wind": {"speed": 2, "deg": 310}, "clouds": {"all": 0}, "dt": 1726759419,
     "sys": {"type": 1, "id": 8928, "country": "RU", "sunrise": 1726717535, "sunset": 1726762511}, "timezone": 10800,
     "id": 504341, "name": "Pskov", "cod": 200}"""

    res_obj = json.loads(st)

    assert(str(extract(res_obj)) == """{"name":"Pskov","coord":{"lon":28.3496,"lat":57.8136},"country":"RU","feels_like (C)":17.68,"timezone":3.0}""")

get_weather_data.__doc__ = '''
Первым аргументом является название города на английском языке. Вторым аргументом является API-ключ OpenWeather. Возвращает актуальную информацию о городе в удобной форме.

The first argument is the name of the city in English. The second argument is the OpenWeather API key. Returns up-to-date information about the city in a convenient form.
'''

