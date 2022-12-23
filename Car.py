# Module par Arthur
import threading
import turtle
from time import sleep
from random import randint
from trait import trait
#from FeuxTricolore import FeuxTricolore
file = r""
# Threading des Voitures
def Car(x, ySol):
    '''
    Paramètres
        x : En bas a gauche de l'image
        ySol : ordonnée du sol du la rue
    Cete fonction dessine un trait horizontale de 3 pixels d'épaisseur
    '''
    while True:
        car = turtle.Turtle()
        car.hideturtle()
        car.up()
        car.goto(0, ySol)
        wait = randint(0, 2)
        sleep(wait)
        voiture = randint(1, 5)
        sens = randint(1, 2)
        if sens == 1:
            car.goto(car.xcor()+500, car.ycor()+18)
            turtle.Screen().addshape('img/Voiture'+ str(voiture)  +'.gif')
            car.shape('img/Voiture'+ str(voiture) +'.gif')
            car.showturtle()
            while car.xcor() >= -500:
                car.goto(car.xcor()-3, car.ycor())

            car.hideturtle()
        if sens == 2:
            car.goto(car.xcor()-500, car.ycor()+18)
            turtle.Screen().addshape('img/Voiture'+ str(voiture)  +'Right.gif')
            car.shape('img/Voiture'+ str(voiture)  +'Right.gif')
            car.showturtle()
            while car.xcor() <= 500:
                car.goto(car.xcor() + 3, car.ycor())
            car.hideturtle()


if __name__ == '__main__':

    trait(-250, -250, 250, -250)
    Car(0, 0)
    # On ferme la fenêtre s'il y a un clique gauche