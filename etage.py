#Module par Theo
from facade import facade
from random import shuffle,randint
from fenetre import fenetre
from fenetreBalcon import fenetreBalcon
import turtle

def etage(x, ySol, couleur, niveau, Fenetre, FenetreBalcon, Finish):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        ySol : ordonnée du sol du la rue
        couleur : couleur de la façade de l'étage
        niveau : numero de l'étage en partant de 0 pour le rdc
    Remarque
       Cette fonction dessine un étage d'un immeuble
    '''
    # dessin des murs
    turtle.speed(10)
    turtle.pencolor(couleur)
    facade(x,ySol,couleur,niveau)

    # dessin des 3 Eléments
    turtle.up()
    turtle.goto(x-70,niveau*60)
    turtle.down()
    for i in range(0, 2+1):
        random=randint(1,2)
        if random==1: #Fenetre
            turtle.pencolor("black")
            fenetre(turtle.xcor()+28, ySol+niveau*60+20, Fenetre, Finish)
        if random==2: #Porte-Fenetre
            turtle.pencolor("black")
            fenetreBalcon(turtle.xcor()+28,ySol+niveau*60+5, FenetreBalcon, Finish)
if __name__ == '__main__':
    etage(0,0,"red",0, "Fenetre","FenetreBalcon")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()