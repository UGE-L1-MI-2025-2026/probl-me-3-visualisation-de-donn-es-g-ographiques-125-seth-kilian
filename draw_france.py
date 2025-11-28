import shapefile
from math import *
from fltk import * 

def draw_france():
    cree_fenetre(1000, 1000)
    sf = shapefile.Reader("departements-20180101")

    for shape_rec in sf.shapeRecords():
        shape = shape_rec.shape
        points = [(i[0]*15+200,i[1]*15-300) for i in shape.points]
        polygone(points, couleur="blue")

    attend_ev()


def mercator(lon, lat):
    R = 1000
    x = R * radians((lon + 180)/360)
    y = (R/2)-(R/2*pi) * log(tan(pi/4 + radians(lat)/2))
    return (x, y)

print(mercator(21.2137, 16.2276)) # Example usage of mercator function 

# draw_france()
# ferme_fenetre()