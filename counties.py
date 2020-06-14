
from geopy.geocoders import Nominatim
address = 'Mecklenburg County, NC'

geolocator = Nominatim(user_agent="nc_explorer")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate are {}, {}.'.format(latitude, longitude))
