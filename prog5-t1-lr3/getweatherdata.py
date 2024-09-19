from owm_key import owm_api_key
import json
import pytz
import datetime


def get_weather_data(place, api_key=None):
    import requests
    s = f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}'
    print(s);
    response = requests.get(s)
    #print(dir(response))
    #print(response.json())
    res_obj = json.loads(response.text)
    ans = extract(res_obj)
        #res = f.read().decode('utf-8')

        #res_obj = json.loads(res)

    # print(res_json)
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

    ans = get_weather_data('Moscow', api_key=owm_api_key)
    assert ans["name"] == "Moscow"
    ans = get_weather_data('Saint Petersburg', api_key=owm_api_key)
    assert ans["cord"]["lon"] == 30.2642
    ans = get_weather_data('Dhaka', api_key=owm_api_key)
    assert ans["timezone"] == 6.0
    assert ans["feels_like (C)"] < 100
    #pass
    # напишите здесь тесты для проверки работы функции как минимум со следующими городами: Москва, Санкт-Петербург, Дакка.
    # какие ещё тесты необходимо здесь написать, чтобы быть уверенным в полном покрытии тестами реализованной функции и
    # соответствии требованиям задачи.


