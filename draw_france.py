import shapefile
from fltk import * 

def draw_france():
    cree_fenetre(1000, 1000)
    sf = shapefile.Reader("departements-20180101")

    for shape_rec in sf.shapeRecords():
        shape = shape_rec.shape
        points = [(i[0]*15, i[1]*15) for i in shape.points]
        polygone(points, couleur="blue")

    attend_ev()
    ferme_fenetre()
