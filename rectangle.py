#Module par Malcolm
import turtle

def rectangle(x,y,w,h):
    '''
    Paramètres
        x, y : coordonnées du centre de la base de rectangle
        w : largeur du rectangle
        h : hauteur du rectangle
    Cette fonction dessine un rectangle Le point de coordonnées (x,y) est
    sur le côté en bas au milieu
    '''
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(w / 2)
    for i in range(0, 2):

        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)
        turtle.forward(w)
    turtle.end_fill()
    pass


if __name__ == '__main__':
    rectangle(0,0,200,100)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()