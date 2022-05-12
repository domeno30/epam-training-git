# Whether v1
# from API https://openweathermap.org/
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here, eg. Armenian
import ch_data_in_xml
owm = OWM('0206cc43eafd2a0aaee3fb76f1839800')
# from API ipstak. Limit of 5000
from ipstack import GeoLookup

geo_lookup = GeoLookup("c5c58628d4b636a6140ba9d88fcd63a5")

lat = 40.158599853515625
lon = 44.499298095703125
#lat =  55.75222
#lon = 37.615555
#lat = geo_lookup.get_own_location()['latitude']
#lon = geo_lookup.get_own_location()['longitude']
#country = geo_lookup.get_own_location()['country_code']
#cap = geo_lookup.get_own_location()['region_name'] + geo_lookup.get_own_location()['country_name']
# print(cap)
# print(location_lon)
#if country == "AM":
#    a = ("Եղանակը Հայաստանում" + ' ')

#if cap == "Yerevan":
#    b = "Ք․ Երևան"
#    print(a + b)
#else:
#    print(cap)

mgr = owm.weather_manager()
observation = mgr.weather_at_place('yerevan,AM')  # the observation object is a box containing a weather object
weather = observation.weather
# print(weather)
# datetime = weather.reference_time()
# print(datetime)

# list_of_locations = reg.locations_for('yerevan', country='AM')
# yerevan = list_of_locations[0]
# lt = yerevan.lat   # 55.75222
# ln = yerevan.lon   # 37.615555
one_call = mgr.one_call(lat, lon, units='metric')

s = one_call.forecast_hourly[3].wind().get('speed', 0)  # Eg.: 4.42

t = one_call.current.temperature()['temp']

feel = one_call.current.temperature()
#
#
# print(feel)

observation = mgr.weather_at_place('yerevan,AM')  # the observation object is a box containing a weather object
# weather = observation.weather
# print(weather)
sd = weather.detailed_status
#if sd = [scattered clouds]
#   dir(sd)



import time
loc = ("Եղանակը Հայաստանում \n" + ' ')
j = ("Ջերմաստիճանը:" + ' ' + str(t) + '' + ' ' + "աստ.: \n")
q = ("Քամու արագությունը \n:  " + str(s) + "   km/h \n")
k = ("Հնարավոր կանխատեսում։  \n" + sd+": \n")

# DATE and TIME
from datetime import datetime
#today = date.today()
    #print()
    #from time import  time
#time_local = "Օր/Ժամ \n" +' '+ datetime.now().isoformat(timespec='minutes')
now = datetime.now()
time_local = "Օր/Ժամ:" +' '+ now.strftime("%d/%m/%y - %H:%M")+ '\n'



