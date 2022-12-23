#Module par Arthur

from couleurAleatoire import couleurAleatoire
from random import randint
from rdc import rdc
from etage import etage
from toit import toit
import turtle

def immeuble(x, ySol, Fenetre, FenetreBalcon, Finish):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
    Cette fonction dessine un immeuble Le nombre d'étage est compris aléatoirement entre 0 et 4
    La couleur de la façade et la couleur de la porte sont tirées au hasard
    '''
    # Nombre d'étage (aléatoire)!!
    nbretage = randint(0, 4) #Definir le nombre d'êtage aleatoire que l'on souhaite
    #Couleurs des éléments (aléatoire)
    couleurporte=couleurAleatoire() #Defini la couleur de la porte
    couleurimmeuble=couleurAleatoire() #Defini la couleur de la facade
    # Dessin du RDC
    rdc(x, ySol, couleurimmeuble, couleurporte, Fenetre, Finish) # Permets de dessiner le RDC en faisant appelle a la fonction
    # Dessin des étages
    for niveau in range(1, nbretage+1): #Permets de faire le nombre d'êtage dessigner par le randint
        etage(x, ySol, couleurimmeuble, niveau, Fenetre, FenetreBalcon, Finish) #Permets de dessiner l'êtage en faisant appelle a la fonction
    # Dessin du toit
    toit(x, ySol, nbretage) #Permets de dessiner l'êtage en faisant appelle au toit


if __name__ == '__main__':
    immeuble(0,-250)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()