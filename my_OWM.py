import pyowm
from pyowm import OWM
from pyowm.utils.config import get_default_config
import configparser



config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here, eg. Russian
owm = OWM('key',config_dict)

city = input('Введите название города:')
mgr = owm.weather_manager()

# Search for current weather in 'city' and get details
try:
    observation = mgr.weather_at_place(city)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]
    wind = w.wind()['speed']
    status = w.detailed_status
    hum = w.humidity
    cloud = w.clouds

    print('В городе ' + city + ' температура сейчас: '+ str(temp) + ' по цельсию')
    print('Также в городе: ' + status)
    print('Скорость ветра: ' + str(wind) + ' м/с')
    print('Относительная влажность: ' + str(hum) + ' %')
    print('Облачность: ' + str(cloud) + ' %')

except (pyowm.commons.exceptions.NotFoundError):
    print('Ошибка! Город не найден.')



