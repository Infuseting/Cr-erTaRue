#Module par Arthur
import turtle
from turtle import Screen
from rectangle import rectangle
from datetime import datetime
def Cycle(ySol):
    '''
    Paramètres :
    remarque :
        Cycle Jour et Nuit
    '''
    Hours = datetime.now().hour

    if Hours >= 9 and Hours <= 17:
        Color1 = (0, 0.74901, 1)
        Color2 = (1, 0.5, 0)
    else:
        Color1 = (0.04705, 0.07843, 0.2705)
        Color2 = (0.1686, 0.1725, 0.3529)
    turtle.speed(10000)
    W, H = Screen().window_width(), Screen().window_height()
    turtle.penup()
    turtle.goto(-W / 2, H / 2)
    turtle.pendown()
    Gradient = [(Grad - Color1[index]) / H for index, Grad in enumerate(Color2)]

    direction = 1


    for distance, y in enumerate(range(H // 2, -H // 2 +100, -1)):
        turtle.forward(W* direction)
        turtle.color([Color1[i] + Gradient * distance for i, Gradient in enumerate(Gradient)])
        turtle.sety(y)

        direction *= -1


    turtle.color("black")
    turtle.fillcolor("brown")
    rectangle(0, ySol, 800, -100)

if __name__ == '__main__':
    Cycle()
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()