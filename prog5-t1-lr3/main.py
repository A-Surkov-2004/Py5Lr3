from owm_key import owm_api_key
import json
from urllib import request
from getweatherdata import get_weather_data

# TODO 1
def get_weather_data(place, api_key=None):

    # использовать библиотеку requests вместо urllib
    with request.urlopen(
            f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}'
    ) as f:
        res = f.read().extract('utf-8')

        res_obj = json.loads(res)

    # print(res_json)

    print((res_obj))

    # with open('data.json', 'w') as f:
    #     json.dump(res_json, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    get_weather_data('Pskov', api_key=owm_api_key)
