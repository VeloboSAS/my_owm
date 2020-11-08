from pyowm import OWM
#from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config


config_dict = get_default_config()
#config_dict = config.get_default_config_for_subscription_type('professional')
config_dict['language'] = 'ru'  # your language here, eg. Russian
owm = OWM('api_key', config_dict)


city = input('Введите название города:')

mgr = owm.weather_manager()

# Search for current weather in 'city' and get details
observation = mgr.weather_at_place(city)
w = observation.weather
temperature = w.temperature('celsius')['temp']
wind = w.wind()['speed']

w.detailed_status         # 'clouds'
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.rain                    # {}
w.heat_index              # None
w.clouds                  # 75


print('В городе ' + city + ' температура сейчас: '+ str(temperature) + ' по цельсию')
print('Также в городе: ' + w.detailed_status)
print('Скорость ветра: ' + str(wind) + ' м/с')
print('Относительная влажность: ' + str(w.humidity) + ' %')


