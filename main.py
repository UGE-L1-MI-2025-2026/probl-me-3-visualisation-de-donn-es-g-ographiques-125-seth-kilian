from shapefile import *

sf = Reader("departements-20180101")

print(sf.records())

