#!/usr/bin/env python
# -*- coding: utf-8 -*-

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from geopandas.tools import geocode
import shapely.speedups




## Build a shape file from Geopandas
addrs = pd.read_csv('data/addressess.txt', sep=";")
addrs.head(2)

geo = geocode(addrs['addr'], provider='nominatim')

geo.head(2)

join = geo.join(addrs)

join.head(2)

# Output file path
fp = "data//addresses.shp"
# Save to Shapefile
join.to_file(fp)

data = gpd.read_file(fp)

print(data.head(2))

gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'


# Filepath to KML file
fp = "data/PKS_suuralue.kml"
polys = gpd.read_file(fp, driver='KML')

polys.head(2)


print("Printing PLots: ")
polys.loc[10]
#shapely.speedups.enable()
southern = polys[polys['Name']=='Kaakkoinen']
#southern = gpd.GeoDataFrame(southern.to_frame())
southern.reset_index(drop=True, inplace=True)

fig, ax = plt.subplots()
polys.plot(ax=ax, facecolor='gray');
southern.head()
print(type(southern))
southern.plot(ax=ax, facecolor='red');
data.plot(ax=ax, color='blue', markersize=5);
plt.tight_layout();
plt.show()
