# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 22:41:12 2019

@author: S533488
"""

from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, GMapOptions
from bokeh.plotting import gmap
from bokeh.plotting import figure
import pandas as pd

netflixLocations = pd.read_pickle('geo_location_longitudesAndLatitudes.pkl')
latitude = []
longitude = []
for tweet in netflixLocations['data']:
    lat = tweet['features']['latitude']
    latitude.append(lat)
for tweet in netflixLocations['data']:
    long = tweet['features']['longitude']
    longitude.append(long)

output_file("gmap.html")
p = figure(plot_width=1000, plot_height=1000, x_range=(-180,180), y_range=(-90,90))


map_options = GMapOptions(lat=5.8837525, lng=44.5202469, map_type="roadmap", zoom=11)


p = gmap("Google Maps API", map_options, title="Netflix mentioned most in these countries across the world")


source = ColumnDataSource(
    data=dict(lat=latitude, 
              lon=longitude)
)

p.circle(x="lon", y="lat", size=15, fill_color="blue", fill_alpha=0.8, source=source)

show(p)