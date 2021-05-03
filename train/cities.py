from os import path
import json


file_path = path.abspath(__file__) 
dir_path = path.dirname(file_path) 
json_file_path = path.join(dir_path,'cities.json')

with open(json_file_path, 'r') as cities:
    CITY_CHOICES = tuple([(city.get('city'), city.get('city')) for city in json.load(cities)])


