#Module par Malcolm
import turtle
from rectangle import rectangle
from trait import trait
from datetime import datetime
from random import randint
def fenetreBalcon(x,y, FenetreBalcon, Finish):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte-fenetre-balcon
        y est l'ordonnée du sol du niveau de la porte-fenetre-balcon
    Remarque:
        Dessine une porte-fenetre avec balcon en 2 temps: la porte fenetre de 30 pixels de large par 50 pixels de hauteur
        puis le balcon
    '''
    # porte-fenetre
    FenetreOn = False
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
    rectangle(x,y,30,50)
    if FenetreOn == True:
        print("Walls", int(x), int(y))
        FenetreBalcon.append(int(x))
        FenetreBalcon.append(int(y))
    turtle.end_fill()
    turtle.fillcolor("")
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    trait(x, y, x, y+50)



    # balcon
    turtle.up()
    turtle.width(3)
    turtle.goto(x-15,y)
    turtle.down()
    rectangle(x,y,40,25)
    turtle.goto(x-20,y)
    for i in range (0,8) :
        trait(turtle.xcor(),turtle.ycor(),turtle.xcor(),turtle.ycor()+25)
        trait(turtle.xcor(), turtle.ycor(), turtle.xcor() + 5, turtle.ycor())
        trait(turtle.xcor(),turtle.ycor(),turtle.xcor(),turtle.ycor()-25)
    turtle.goto(x+15, y)
    turtle.width(1)


    pass



if __name__ == '__main__':
    fenetreBalcon(0,0, "FenetreBalcon")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()