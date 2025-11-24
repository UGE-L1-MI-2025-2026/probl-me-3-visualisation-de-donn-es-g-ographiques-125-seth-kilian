from shapefile import *

sf = Reader("departements-20180101.shp")

print(sf.records())

