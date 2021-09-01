import mysql.connector


class PlacesModel:
    def __init__(self):
        self.cnx = mysql.connector.connect(user='tragent-db', password='eded....', host='34.136.75.172', database='tragent')

    def write(self,data):
        city = data["city"] if "city" in data else ""
        place_type = data["type"] if "type" in data else ""
        name = data["name"] if "name" in data else ""
        address = data["address"] if "address" in data else ""
        lat = data["lat"] if "lat" in data else 0
        lng = data["lng"] if "lng" in data else 0
        business_status = data["business_status"] if "business_status" in data else "open"
        phone_number = data["phone_number"] if "phone_number" in data else ""
        google_map_place_id = data["google_map_place_id"] if "google_map_place_id" in data else ""
        rating = data["rating"] if "rating" in data else -1
        ratings_total = data["ratings_total"] if "ratings_total" in data else -1
        website = data["website"] if "website" in data else ""
        opening_hours = data["opening_hours"] if "opening_hours" in data else "{}"


        cursor = self.cnx.cursor()
        add_employee = ("INSERT INTO places "
               "(city, type, name, address, lat, lng, business_status, phone_number, google_map_place_id, rating, ratings_total, website, opening_hours) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data_employee = (city,place_type,name,address,lat,lng,business_status,phone_number,google_map_place_id,rating,ratings_total,website,opening_hours)
        cursor.execute(add_employee, data_employee)
        self.cnx.commit()
        cursor.close()

    def find_place(self,place_id):
        cursor = self.cnx.cursor(buffered=True)
        find_place_query = ("SELECT city, type, name, address, lat, lng, business_status, phone_number, google_map_place_id, rating, ratings_total, website, opening_hours FROM places WHERE google_map_place_id = %s")
        cursor.execute(find_place_query,(place_id,))
        self.cnx.commit()
        for (city, type, name, address, lat, lng, business_status, phone_number, google_map_place_id, rating, ratings_total, website, opening_hours) in cursor:
            data = {}
            data["city"] = city
            data["type"] = type
            data["name"] = name
            data["address"] = address
            data["lat"] = lat
            data["lng"] = lng
            data["business_status"] = business_status
            data["phone_number"] = phone_number
            data["google_map_place_id"] = google_map_place_id            
            data["rating"] = rating
            data["ratings_total"] = ratings_total
            data["website"] = website
            data["opening_hours"] = opening_hours
        cursor.close()
        return data

    def done(self):
        self.cnx.close()

# Example
# data = {}
# data["city"] = "Toronto"
# data["type"] = "Hotpot!"
# data["name"] = "Yiyi Huoguo"
# data["address"] = "Fifth Ave"
# data["lat"] = -37.14
# data["lng"] = 122.389
# data["business_status"] = "open"
# data["phone_number"] = "1234567890"
# data["google_map_place_id"] = "blah"
# data["rating"] = 4.2
# data["ratings_total"] = 500
# data["website"] = "www.google.com"
# data["opening_hours"] = '{}'
# mysqlcon = PlacesModel()
# data = mysqlcon.find_place("ChIJ95syPVV-j4AReUabNI0D0hc")
# print(data)
# mysqlcon.done()



