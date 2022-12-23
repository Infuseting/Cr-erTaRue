#Module par Theo
from facade import facade
from random import randint
from porte import porte
from fenetre import fenetre
import turtle

def rdc(x, ySol, c_facade, c_porte, Fenetre, Finish):
    '''
    Paramètres
        x : (int) abscisse du centre
        ySol : ordonnée du sol du la rue
        c_facade : couleur de la façade
        c_porte : couleur de la porte
    remarque:
        Cette fonction dessine le rdc en 2 étapes
        D'abord la façade
        Puis les 3 élements : 1 porte et 2 fenêtres disposées au hasard
    '''
    # Dessine la facade
    turtle.pencolor(c_facade)
    facade(x, ySol, c_facade, 0)

    # Construit les 3 éléments (1 porte et 2 fenetres)
    porterandom=randint(0 ,2)
    turtle.goto(turtle.xcor()-140, turtle.ycor())

    for i in range(0 ,2+1):
        if i == porterandom:
            turtle.pencolor("black")
            porte(turtle.xcor()+28, ySol, c_porte)
        else:
            turtle.pencolor("black")
            fenetre(turtle.xcor()+28, ySol+20, Fenetre, Finish)


if __name__ == '__main__':
    rdc(0,0,"red","green", "Fenetre")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()