from birdy.twitter import UserClient
from geopy.geocoders import Nominatim
import json

# user inputs
radius = input("enter a radius ex: 1mi, 15mi:  ->")
address = input("enter an address. ex: 123 fake street Houston, TX 77006:  ->")
query = input("enter a search query. ex: hurricane harvey 2017:  ->")

# GeoLocation
geolocator = Nominatim()
location = geolocator.geocode(address)

address = location.address
coordinates = "{} {}".format(location.latitude, location.longitude)

client = UserClient(
    "ekYpdh37MmkQWTcrG484zgwXw",
    "AMHi5d8hEOfDLDJexKpnvqj2YOzAwxLPkotqEEkR81NaFdYseK",
    "609379206-usySeSFiB9nqMZRkmIxWolvscDVl22m1rB9v6RFM",
    "KFSMqHyOcLL5PHKynpVwsnPv4E1tIQi5yszf8ijh69zs2"
)

 # Query List
#############
# until
# since_id
# lang
# q
# geocode
#############


# response params
resource = client.api.search.tweets
geocode = "{} {}".format(coordinates, radius)

response = resource.get(q=query,geocode=geocode)

response_data = response.data           # decoded JSON data
response_url = response.resource_url   # resource URL
respnose_headers = response.headers        # dictionary containing response HTTP headers

print(response_data)
