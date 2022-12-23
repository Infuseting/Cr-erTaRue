import turtle

def trait(x1,y1,x2,y2):
    '''
    Paramètres
        x1, y1 : coordonnées du début du trait
        x2, y2 : coordonnées de la fin du trait
    Cette function dessine un trait entre les 2 points transmis en paramètres
    '''
    turtle.up() #Permet de lever le stylo
    turtle.goto(x1, y1) #Permet de se deplacer vers le 1er point du segment
    turtle.down() #Permet de baisser le stylo
    turtle.goto(x2, y2) #Permets de tracer le trait jusqu'a x2, y2
    pass

if __name__ == '__main__':
    # dessine deux traits
    trait(-50,-50,100,100)
    trait(0, 100, 0, -100)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
