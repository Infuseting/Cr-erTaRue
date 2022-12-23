#Module par Malcolm
import turtle
from random import randint

def couleurAleatoire():
    '''
    renvoie un triplet de 3 nombres entier compris entre 0 et 255
    Ce triplet correspond à une couleur codée en RVB
    '''
    turtle.colormode(255)
    Color1 = int(randint(0, 255))
    Color2 = int(randint(0, 255))
    Color3 = int(randint(0, 255))

    return Color1, Color2, Color3

