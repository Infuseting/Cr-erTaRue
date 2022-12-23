#Module par Arthur
from random import randint
from toit1 import toit1
from toit2 import toit2
import turtle

def toit(x, ySol, niveau):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        ySol: ordonnée du sol
        niveau : numéro de l'étage en partant de 0 pour le rdc
    Cette fonction dessine au hasard un des 2 types de toit

    '''
    random = randint(1, 2)
    if random == 1:
        toit1(x, ySol, niveau)
    if random == 2:
        toit2(x, ySol, niveau)
    pass

if __name__ == '__main__':
    toit(0,0,0) 
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()