from search_nearby import Place
from city_points import CityPoints

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
        for city_point in city_points.generate_points(self.city_points_radius):
            place = Place(city_point)
            place.search_place_nearby(self.search_nearby_radius, place_type, page_token="")
            for place_details in place.place_details_list:
                self.all_places_details.append(place_details)


# Example
# crawler = Crawler("San Francisco", 200, ["bar","restaurant"])
# crawler.get_all_types_of_places()
# print(crawler.all_places_details)