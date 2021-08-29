from search_nearby import Place
from city_points import CityPoints
from model import PlacesModel
import json


class Crawler:
    # city: the city we need to crawl for
    # search_nearby_radius
    # place_types: a list of place types for the given location
    def __init__(self, city, search_nearby_radius, place_types):
        self.city = city
        self.search_nearby_radius = search_nearby_radius # 1m
        self.city_points_radius = search_nearby_radius / 100000 * 1.414 # 100km
        self.place_types = place_types
        self.all_places_details = []

    def get_all_types_of_places(self):
        for place_type in self.place_types:
            self.get_one_type_of_places(place_type)
            

    def get_one_type_of_places(self, place_type):
        city_points = CityPoints(self.city)
        mysqlcon = PlacesModel()

        for city_point in city_points.generate_points(self.city_points_radius):
            place = Place(city_point)
            place.search_place_nearby(self.search_nearby_radius, place_type, page_token="")
            for place_details in place.place_details_list:
                self.all_places_details.append(place_details)
                print(place_details)
                data = {}
                data["city"] = self.city
                data["type"] = place_type
                data["name"] = place_details.get("name") or ""
                data["address"] = place_details.get("formatted_address") or ""
                data["lat"] = place_details["geometry"]["location"]["lat"]
                data["lng"] = place_details["geometry"]["location"]["lng"]
                business_status = place_details.get("business_status") or ""
                data["business_status"] = "True" if business_status=="OPERATIONAL" else "False"
                data["phone_number"] = place_details.get("formatted_phone_number") or ""
                data["google_map_place_id"] = place_details["place_id"]
                data["rating"] = place_details.get("rating") or -1
                data["ratings_total"] = place_details.get("user_ratings_total") or 0
                data["website"] = place_details.get("website") or ""
                data["opening_hours"] = json.dumps(place_details.get("opening_hours") or {})
                mysqlcon.write(data)
                return
        mysqlcon.done()


# Example
# crawler = Crawler("San Francisco", 200, ["amusement_park","aquarium","bakery","book_store","museum","park","shopping_mall","tourist_attraction","university"])
# crawler.get_all_types_of_places()
