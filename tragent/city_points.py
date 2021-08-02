import json
# from shapely.geometry import Point
# from shapely.geometry.polygon import Polygon

class Point:
	def __init__(self, lat, lng):  
		self.lat = lat
		self.lng = lng


class CityPoints:
	# init method or constructor   
	def __init__(self, city):  
		self.city = city
		self.points = []
		self.polygon = None

	def get_polygon(self):
		with open('./city_boundaries/San Francisco.json') as json_file:
			data = json.load(json_file)
			return [tuple(point) for point in data['coordinates'][0]]



	# def intersect(self, point_A, point_B, point_C, point_D):
	# 	pax = point_A.lat
	# 	pay = point_A.lng
	# 	pbx = point_B.lat
	# 	pby = point_B.lng
	# 	pcx = point_C.lat
	# 	pcy = point_C.lng
	# 	pdx = point_D.lat
	# 	pdy = point_D.lng


	# def get_points(self):



# point = Point(0.5, 0.5)
# polygon = Polygon([(0, 0), (0, 1), (1, 1), (1, 0)])

San = CityPoints('San')
print(San.get_polygon())
