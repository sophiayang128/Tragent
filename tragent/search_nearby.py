import googlemaps
import time
from auth import Auth
from place_details import Details

class Place:

    page_token = ""


    def __init__(self, location):
        self.key = Auth.get_api_key()
        self.client = googlemaps.Client(self.key)
        self.language = "en-AU"
        self.region = "AU"
        self.rank_by = "distance"
        self.location = location
        self.place_details_list = []


    def search_place_nearby(self, radius, place_type, page_token):
        if page_token == "":
            response = self.client.places_nearby(
                            location=self.location,
                            radius=radius,
                            open_now=True,
                            type=place_type
                        )
        else:
            time.sleep(2) # Sleep to avoid too quick request
            response = self.client.places_nearby(page_token=page_token)
        for result in response['results']:
            place_details = Details().get_place_details(place_id=result['place_id'])
            self.place_details_list.append(place_details)
        if 'next_page_token' in response:
            self.search_place_nearby(radius, place_type, response['next_page_token'])
        else:
            return

# Example
location = (37.80865824324315, -122.40926971224243)
p1 = Place(location)
p1.search_place_nearby(1500, "aquarium", "")
print(p1.place_details_list)


# 1. Lat,lon, type -> []
# 2. Based on metadata, do filtering
