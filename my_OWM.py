from pyowm import OWM
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config


config_dict = get_default_config()
#config_dict = config.get_default_config_for_subscription_type('professional')
config_dict['language'] = 'ru'  # your language here, eg. Russian
owm = OWM('6d00d1d4e704068d70191bad2673e0cc', config_dict)


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
#print(w.rain)
print('Также в городе: ' + w.detailed_status)
print('Скорость ветра: ' + str(wind) + ' м/с')
print('Относительная влажность: ' + str(w.humidity) + ' %')
print('Скорость ветра: ' + str(w.clouds ) + ' м/с')


#Weather forecasts

daily_forecaster = mgr.forecast_at_place(city, 'daily')
tomorrow = timestamps.tomorrow()                                   # datetime object for tomorrow
weather_daily = daily_forecaster.get_weather_at(tomorrow)


print(weather_daily)
#print(three_h_forecast)





