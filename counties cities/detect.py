#detects counties without cities

import pandas as pd

counties = pd.read_csv('County.csv')
cities = pd.read_csv('City.csv')

county_ids = set(counties['_id'])
city_county_ids = set(cities['countyId'])

no_city_counties = county_ids - city_county_ids

no_city_df = counties[counties['_id'].isin(no_city_counties)]

print(no_city_df['county'])