import googlemaps
from auth import Auth

class Details:

    def __init__(self):
        self.key = Auth.get_api_key()
        self.client = googlemaps.Client(self.key)
        self.fields = ["business_status",
                       "geometry/location",
                       "place_id",
                       "opening_hours",
                       "formatted_phone_number",
                       "formatted_address",
                       "name",
                       "rating",
                       "user_ratings_total",
                       "website"]

    def get_place_details(self, place_id):
        response = self.client.place(
                        place_id,
                        fields=self.fields)
        return response['result']
