#Module Par Theo
import turtle
from trait import trait

def toit2(x, ySol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        ySol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit plat d'épaisseur 10 pixels et mesurant 140 pixels de large
    '''
    turtle.up()
    turtle.goto(x, ySol+niveau)
    turtle.down()
    turtle.width(10)
    trait(-70+x,ySol+niveau*60+60+2,x+70,ySol+niveau*60+60+2)
    turtle.width(1)




if __name__=='__main__':
    toit2(0,0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()