#Module par Theo
from rectangle import rectangle
import turtle
from datetime import datetime
from random import *
def fenetre(x,y, Fenetre, Finish):
    '''
    Paramètres :
        x est l'abcisse du centre de la fenêtre
        y est l'ordonnée du sol du niveau de la fenetre
    Remarque:
        dessine une fenetre de 30 pixels sur 30 pixels

    '''
    FenetreOn=False
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    Hours = datetime.now().hour
    if Hours >= 9 and Hours <= 17:
        turtle.fillcolor("cyan")
    else:
        light = randint(1, 2)
        if light == 1:
            turtle.fillcolor(253, 239, 205)
        if light == 2:
            turtle.fillcolor(47, 29, 50)
            FenetreOn = True
    if Finish == True:
        turtle.fillcolor(253, 239, 205)
    turtle.begin_fill()

    rectangle(x, y,30,30)
    if FenetreOn == True:
        print("Walls", int(x), int(y))
        Fenetre.append(int(x))
        Fenetre.append(int(y))
    turtle.end_fill()
    FenetreOn = False



if __name__ == '__main__':
    fenetre(0,150)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()