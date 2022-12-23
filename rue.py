#Avant de commencer plusieurs fonctionnalités sont rajoutées par notre groupe.
#Il faut savoir que chaqu'une des fonctions à son auteur de precisé (Pour faciliter la note)
#Il y a donc plusieurs fonctionnalités ajoutées
#Le Cycle Jour/Nuit entre 9h et 17h il fera Jour et entre 17h et 9h il fera Nuit. Cette fonctionnalité utilise uniquement le module datetime
#Les Fenetres et Les FenetresBalcons sont standart entre 9h et 17h mais peuvent être aleatoirement colorée entre Jaune (Comme si la lumiere êtait allumé et Noir comme si la lumiere êtait eteints) entre 17h et 9h
#Les voitures passeront continuellement sans s'arreter. Il y a un total de 5 type de vehicule differents.
#Un cercle une fonctionnalité inutile mais quand même rajouté car on souhaitait l'utilisé mais nous n'avons pas eu le temps. Le cercle peux être d'un rayon differents a des coordonnées differentes, couleur differentes et pour finir la circonferences qu'il peut y avoir 180° par exemple
#Pour finir nous avons rajouté un personnage jouable pouvant aller a gauche ou a droite indefiniment. Vous pouvez le bouger a l'aide des fleches directionelles
import turtle
from sol import sol
from immeuble import immeuble
from Cycle import Cycle
from Car import Car
from fenetreBalcon import fenetreBalcon
from fenetre import fenetre
from Personnage import personnage

# ------------------------------
# ------------------------------
# ------------------------------
Fenetre = []
FenetreBalcon = []
def main():
    turtle.setup(800, 600)
    turtle.title("Dessine ta Rue !")
    turtle.speed(2000)
    global Reveille
    Reveille= False
    global Finish
    Finish = False
    turtle.listen()
    turtle.onkey(Reload, "Escape")
    # On définit la hauteur du sol
    y_sol = -200
    #Le ciel
    Cycle(y_sol)
    # Dessin du sol de la rue
    sol(y_sol)

    turtle.up()
    pos=-500+40
    turtle.down()
    # Dessin des 4 immeubles
    for i in range(1, 4+1):
        immeuble(pos+i*180, y_sol, Fenetre, FenetreBalcon, Finish)
    Finish = True
    print("Fenetre :",Fenetre[0:])
    print("Fenetre Balcon:", FenetreBalcon[0:])
    print("Len Fenetre " + str(len(Fenetre)))
    print("Len Fenetre Balcon " + str(len(FenetreBalcon)))


    #turtle.onscreenclick(reveille)

    #Les voitures qui defilent
    personnage(y_sol)
    Car(0, y_sol)


    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()

#Module par Arthur
def Reload():
    turtle.bye()
    print("Close !")


#Module par Arthur (Peux être tester mais ne fonctionne pas parfaitement)
def reveille(x, y):
    global Reveille
    print(x, y)
    if Reveille == False:
        turtle.hideturtle()
        x = int(x)
        y = int(y)
        Reveille = True
        for i in range(1, int((len(Fenetre))//2)+1):
            for p in range(0, 30+1):

                if x-p == int(Fenetre[i*2-2]):

                    for i in range(1, int((len(Fenetre)) // 2) + 1):
                        for e in range(0, 30+1):
                            if y - e == int(Fenetre[i * 2-1]):

                                y -= e
                                x -= p
                                fenetre(x, y, Fenetre, Finish)
                                Reveille = False
                                exit()


        for i in range(1, int((len(FenetreBalcon))//2)+1):
            for p in range(0, 30+1):
                if x-p == int(FenetreBalcon[i*2-2]):

                    for i in range(1, int((len(FenetreBalcon))//2)+1):
                        for u in range(0, 50+1):
                            if y-u == int(FenetreBalcon[i*2-1]):

                                y-=u
                                x-=p
                                fenetreBalcon(x, y, FenetreBalcon, Finish)
                                Reveille = False
                                exit()
        Reveille = False


if __name__ == '__main__':
    main()



