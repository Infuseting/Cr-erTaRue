# Module par Arthur
import turtle
# ----- Sol de la rue -----
def Circle(x, ySol, r, degres, color):
    '''
    Paramètres
        y_sol : ordonnée du sol du la rue
        x : abscisse du centre de l'étage
        r: rayon du cercle
        degres: Degres du cercle (180 pour un demi-cercle)
        color: Couleur de l'interieur du cercle

    Cete fonction dessine un cercle
    '''
    turtle.up()
    turtle.goto(x, ySol)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r, degres)
    turtle.end_fill()
    pass


if __name__ == '__main__':
    Circle(0, 0, 20, 90)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()