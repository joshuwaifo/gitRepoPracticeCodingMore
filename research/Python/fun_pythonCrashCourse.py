# obtain the data using the following terminal command
# curl https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson --output eq_1_day_m1.json

import json

# Explore the structure of the data.
# filename_type_str = 'data/eq_1_day_m1.json'
filename_type_str = 'data/eq_data_30_day_m1.json'
with open(filename_type_str) as f:
    all_eq_data = json.load(f)



all_eq_dicts_type_list = all_eq_data['features']
print(len(all_eq_dicts_type_list))


magnitudes_type_list, longitudes_type_list, latitudes_type_list, hover_texts_type_list = [], [], [], []
for eq_dict_type_dict in all_eq_dicts_type_list:
    magnitude_type_float = eq_dict_type_dict['properties']['mag']
    longitude_type_float = eq_dict_type_dict['geometry']['coordinates'][0]
    latitude_type_float = eq_dict_type_dict['geometry']['coordinates'][1]
    title_type_str = eq_dict_type_dict['properties']['title']
    magnitudes_type_list.append(magnitude_type_float)
    longitudes_type_list.append(longitude_type_float)
    latitudes_type_list.append(latitude_type_float)
    hover_texts_type_list.append(title_type_str)


print(magnitudes_type_list[:10])
print(longitudes_type_list[:5])
print(latitudes_type_list[:5])
readable_file_type_str = 'data/readable_eq_data.json'
with open(readable_file_type_str, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

# note that it is (latitude, longitude) but visually speaking (y, x) in the web based pllot
# therefore I guess it could be said x is longitude, y is latitude
# as a nice visual reminder, use latitude is close to altitude which is a word I'm more comfortable with for height
from plotly import offline
from plotly import graph_objs

# map the earthquakes.
data_type_list = [graph_objs.Scattergeo(lon=longitudes_type_list, lat=latitudes_type_list)]
my_layout_type_Layout = graph_objs.Layout(title='Global Earthquakes')

# clean up magnitudes list
magnitudes_type_list = [0 if magnitude_type_float is None or magnitude_type_float <= 0 else magnitude_type_float for magnitude_type_float in magnitudes_type_list]


data = [{
    'type': 'scattergeo',
    'lon':longitudes_type_list,
    'lat':latitudes_type_list,
    'marker':{
        'size': [5*magnitude_type_float for magnitude_type_float in magnitudes_type_list],
        'color': magnitudes_type_list,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {
            'title': 'Magnitude'
        }
    }
}]

fig_type_dict = {
    'data': data,
    'layout': my_layout_type_Layout
}

# open a browser window with a 'map' of the world with earthquakes that have occurred in the last 24 hours of when the data was retrieved plotted as a circle
offline.plot(fig_type_dict, filename='global_earthquakes.html')


from plotly import colors
for key_type_str in colors.PLOTLY_SCALES.keys():
    print(key_type_str)