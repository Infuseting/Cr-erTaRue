#Module Par Noah
import turtle
from trait import trait

def toit1(x, ySol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        ySol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit triangulaire noir de base 160 pixels
    et de hauteur centrale 40 pixels
    '''
    turtle.up()
    turtle.goto(x, ySol+niveau*60+60)
    turtle.down()
    turtle.begin_fill()
    turtle.fillcolor("black")
    trait(turtle.xcor()-80, turtle.ycor(), turtle.xcor()+80, turtle.ycor())
    trait(turtle.xcor(), turtle.ycor(), x, ySol+niveau*60+40+60)
    trait(turtle.xcor(), turtle.ycor(), turtle.xcor()-80, turtle.ycor()-40)
    turtle.end_fill()
    pass


if __name__ == '__main__':
    toit1(0,0,0)
    # On ferme la fenêtre s'il y a un clic gauche
    turtle.exitonclick()
