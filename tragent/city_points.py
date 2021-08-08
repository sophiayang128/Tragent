import json
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

class CityPoints:
	# init method or constructor   
	def __init__(self, city):  
		self.city = city
		self.points = []
		self.polygon = None

	def get_polygon_points(self):
		with open(f'./data/city_boundaries/{self.city}.json') as json_file:
			data = json.load(json_file)
			self.points = [tuple(point) for point in data['coordinates'][0]]
			return self.points

	def generate_poly(self):
		self.polygon = Polygon(self.get_polygon_points())

	def generate_points(self, radius):
		self.generate_poly()
		max_lat = max([p[0] for p in self.points])
		min_lat = min([p[0] for p in self.points])

		max_lng = max([p[1] for p in self.points])
		min_lng = min([p[1] for p in self.points])

		n_rows = int((max_lat - min_lat) // radius)
		n_cols = int((max_lng - min_lng) // radius)
		print("number of rows:", n_rows)
		print("number of cols:", n_cols)
		points = []
		for i in range(n_rows):
			for j in range(n_cols):
				point = (min_lat + radius * i, min_lng + radius * j)
				if self.polygon.contains(Point(point[0], point[1])):
					points.append(point)
		print("number of points: ", len(points))
		return points


# Example
# San = CityPoints('San Francisco')
# print(San.generate_points(0.01))
