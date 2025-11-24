from shapefile import *
from fltk import *

cree_fenetre(1000, 1000)
sf = Reader("departements-20180101")

print(sf.records())

seine_et_marne = sf.shape(47)
print(seine_et_marne.bbox)

points = [(i[0]*20, i[1]*20) for i in seine_et_marne.points]

polygone(points, couleur="blue")
attend_ev()
ferme_fenetre()