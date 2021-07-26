import googlemaps
from datetime import datetime

class Place:

    page_token = ""


    def __init__(self, location):
        self.key = 'AIzaSyD6unBfajZZK3w4UavRHBt9BhEw4veoxNI'
        self.client = googlemaps.Client(self.key)
        self.language = "en-AU"
        self.region = "AU"
        self.rank_by = "distance"
        self.location = location
        self.place_list = []


    def search_place_nearby(self, radius, place_type, page_token):
        response = {}
        if page_token == "":
            response = self.client.places_nearby(
                            location=self.location,
                            radius=radius,
                            open_now=True,
                            type=place_type
                        )
            # print(response['results'])
        else:
            print(page_token)
            response = self.client.places_nearby(page_token=page_token)
        self.place_list.append(response['results'])
        if 'next_page_token' in response:
            self.search_place_nearby(radius, place_type, response['next_page_token'])
        else:
            return


location = (37.7896451, -122.3897223)
p1 = Place(location)
p1.search_place_nearby(1000, "restaurant", "")


# 1. Lat,lon, type -> []
# 2. Based on metadata, do filtering
