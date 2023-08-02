#detects cities without countiy
import pandas as pd

counties = pd.read_csv('County.csv')  
cities = pd.read_csv('City.csv')

city_county_ids = set(cities['countyId'])
county_ids = set(counties['_id'])

no_county_cities = city_county_ids - county_ids

no_county_df = cities[cities['countyId'].isin(no_county_cities)]

print(no_county_df['cities'])