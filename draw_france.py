import shapefile
from math import *
from fltk import * 

def mercator(long, lat):
    x = long
    y = degrees(log(tan(radians(lat) / 2 + pi / 4)))
    return x, y

def calcule_parametres(x_min, y_min, x_max, y_max, X_orig, Y_orig, W, H):

    a_abscisses = W / (x_max - x_min)
    a_ordonnees = H / (y_max - y_min)

    a = min(a_abscisses, a_ordonnees)

    B=X_orig - a * x_min
    C=Y_orig + a * y_max

    return a, B, C

def place_point(x, y, a, B, C):
    X = a * x + B
    Y = - a * y + C
    return X, Y 
    

    

sf = shapefile.Reader("departements-20180101")
dept = sf.shape(50)
long_min, lat_min, long_max, lat_max = dept.bbox
# ile = dept.parts[0]

points_mercator = [mercator(long, lat) for long, lat in dept.points]

x_min, y_min = mercator(long_min, lat_min)
x_max, y_max = mercator(long_max, lat_max)

largeur_fenetre, hauteur_fenetre = 800, 600
a, B, C = calcule_parametres(x_min, y_min, x_max, y_max, 50, 50, largeur_fenetre, hauteur_fenetre)

point_places = [place_point(x, y, a, B, C) for x, y in points_mercator]

cree_fenetre(1000, 1000)
polygone(point_places)
attend_ev()
ferme_fenetre()

