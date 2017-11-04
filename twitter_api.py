from birdy.twitter import UserClient
from geopy.geocoders import Nominatim
import json
import datetime


# Create twitte client
client = UserClient(
    "ekYpdh37MmkQWTcrG484zgwXw",
    "AMHi5d8hEOfDLDJexKpnvqj2YOzAwxLPkotqEEkR81NaFdYseK",
    "609379206-usySeSFiB9nqMZRkmIxWolvscDVl22m1rB9v6RFM",
    "KFSMqHyOcLL5PHKynpVwsnPv4E1tIQi5yszf8ijh69zs2"
)

# user inputs
radius = input("enter a radius ex: 1mi, 15mi:  ->")
address = input("enter an address. ex: 123 fake street Houston, TX 77006:  ->")
query = input("enter a search query. ex: hurricane harvey 2017:  ->")
# since_id = input("enter a start date. ex: 2017-11-03 ")
# until = input("enter an end date. ex: 2017-11-03 ")

# GeoLocation
# geolocator = Nominatim()
# def gen_location(address):
#     if address:
#         return geolocator.geocode(address)
#     else:
#         return gen_location(input("no address found. please enter address"))
# GEOCODE
# location = gen_location(address)
# coordinates = "{} {}".format(location.latitude, location.longitude)
# geocode = "{} {}".format(coordinates, radius)


# Date

# def validate_date_range(date1, today):
#     if end < start:
#         print("invalid date range")
#     else:
#         print("{} - {}".format(start, end))
#
# # test inputs
# end = datetime.date(2017, 5, 23)
# start = datetime.date(2017, 4, 23)
# validate_date_range(start, end)


# response params
resource = client.api.search.tweets

# Query List
#############
# until
# since_id
# lang https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
# q
# geocode
#############

# generate payload
# def gen_payload(**kwargs):
#     payload = []
#     for key, value in kwargs.items():
#         if value:
#             payload.append()
#             print("key: {} value: {}".format(key, value))
#
# gen_payload(keywords=query,geocode=geocode,since_id=since_id,until=until)

response = resource.get(q=query, lang="en")

response_data = response.data           # decoded JSON data
response_url = response.resource_url   # resource URL
response_headers = response.headers        # dictionary containing response HTTP headers


statuses = response_data['statuses']

print(statuses)

for status in statuses:
    created_at = status['created_at']
    text = status['text']
    coordinates = status['coordinates']
    place = status['place']
    retweet_count = status['retweet_count']
    lang = status['lang']
    # lists
    hashtags = status['entities']['hashtags']
    user_mentions = status['entities']['user_mentions']
    urls = status['entities']['urls']
    user = status['user']
    # print("#" * 50)
    # print("text: {}".format(text))
    # print(coordinates)
    # print(place)

#statuses = json.dumps(response_data)
