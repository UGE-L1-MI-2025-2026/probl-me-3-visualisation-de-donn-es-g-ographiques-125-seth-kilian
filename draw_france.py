import shapefile
from math import *
from fltk import * 

def draw_france():
    # cree_fenetre(1000, 1000)
    # sf = shapefile.Reader("departements-20180101")

    # for shape_rec in sf.shapeRecords()[:3]:
    #     shape = shape_rec.shape
    #     points = shape.points
    #     print(points[:10])
    #     points = [mercator(lon, lat) for lon, lat in points]
    #     print(points[:10])
    #     points = [(x + 500, 500 - y) for x, y in points]  # Centering the map
    #     print(points[:10])
    #     polygone(points, couleur="blue")
        

    # attend_ev()


# def mercator(lon, lat):
    """x = radians((lon + 180)/360)
    y = -pi * log(tan(pi/4 + radians(lat)/2))
    return (x, y)"""

# print(mercator(81.2137, 6.2276)) Example usage of mercator function 

# draw_france()
# ferme_fenetre()

sf = shapefile.Reader("departements-20180101")
print(sf.shape().bbox)
print(sf.shape(0).bbox)
print(sf.shape(1).bbox)

x_min = sf.shape().bbox[0]
y_min = sf.shape().bbox[1]

for i in sf.shape().bbox:


    

    # return (x_min, y_min, x_max, y_max)
