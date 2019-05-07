### https://github.com/Python-GIS/latest/tree/master/data

import geopandas as gpd
%matplotlib inline
import matplotlib.pyplot as plt
import pysal as ps
# Filepath
fp = "AutoGIS/IntroToPythonGIS/Lesson4/data/Vaestotietoruudukko_2015/Vaestotietoruudukko_2015.shp"

# Read the data
pop = gpd.read_file(fp)

pop.head(2)

# Change the name of a column
pop = pop.rename(columns={'ASUKKAITA': 'pop15'})

pop.columns

selected_cols = ['pop15', 'geometry']
pop = pop[selected_cols]

pop.tail(2)


addrs = gpd.read_file('AutoGIS/IntroToPythonGIS/Lesson4/data/addresses.shp')

addrs.crs
pop.crs

#pop.crs = {'ellps': 'GRS80','k': 1,'lat_0': 0,'lon_0': 25,'no_defs': True,'proj': 'tmerc','units': 'm' ,'x_0': 25500000,'y_0': 0}
print(pop.head(2))
#print(pop.head(2), pop.crs)
#addrs.crs ={'ellps': 'GRS80','k': 1,'lat_0': 0,'lon_0': 25,'no_defs': True,'proj': 'tmerc','units': 'm' ,'x_0': 25500000,'y_0': 0}
addrs = addrs.to_crs(epsg = 3879)
addrs.crs
pop = pop.to_crs(epsg = 3879)
print(pop.head(2))
print(addrs.crs)
print(addrs.head(2))
addrs.crs == pop.crs

addrs.to_file('AutoGIS/IntroToPythonGIS/Lesson4/data/Reprojected/addresses_epsg3879.shp')
join = gpd.sjoin(addrs, pop, how="inner", op="within")

join

join.to_file('AutoGIS/IntroToPythonGIS/Lesson4/data/Reprojected/addresses_pop15_epsg3979.shp')

import matplotlib.pyplot as plt


join.plot(column='pop15', cmap="Reds", markersize=7,legend=True);

print(type(join))
