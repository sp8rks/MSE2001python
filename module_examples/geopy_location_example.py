# from geopy.geocoders import Nominatim
# address='Springfield'
# geolocator = Nominatim(user_agent="Your_Name")
# location = geolocator.geocode(address,timeout=None)
# print(location.address)
# print((location.latitude, location.longitude))

# # %%
# from  geopy.geocoders import Nominatim
# geolocator = Nominatim(user_agent="Your_Name")
# city ="Agra"
# country ="India"
# loc = geolocator.geocode(city+','+ country)
# print("latitude is :-" ,loc.latitude,"\nlongtitude is:-" ,loc.longitude)

# UFO = [29.8830556,97.9411111]


# %%
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Your_name")
#my city
location = geolocator.reverse("40.6868914, -111.8754907", timeout=None)
#camp loll
#location = geolocator.reverse("44.1093, 110.8572", timeout=None)
print("The Garden of Eden is",location.raw['address']['city'])
