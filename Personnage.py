#Module par Arthur
import turtle
def personnage(ySol):
    '''
    Paramètres :
        ySol : Coordonnées du sol
    Remarque:
        dessine une fenetre de 30 pixels sur 30 pixels

    '''
    global Coord
    Coord = ySol+20
    global RightVar
    RightVar = 1
    global LeftVar
    LeftVar = 1
    global PersonnageVar
    PersonnageVar = turtle.Turtle()
    PersonnageVar.up()
    turtle.listen()
    turtle.onkey(Left, "Left")
    turtle.onkey(Right, "Right")
    PersonnageVar.goto(0, Coord)
    turtle.Screen().addshape('img/personnage/Stay.gif')
    PersonnageVar.shape('img/personnage/Stay.gif')


def Left():
    global RightVar
    global LeftVar
    if int(RightVar) >= 1:
        RightVar = 1
    if int(LeftVar) > 4:
        LeftVar = 1
    turtle.Screen().addshape('img/personnage/Walk'+ str(LeftVar)+'.gif')
    PersonnageVar.shape('img/personnage/Walk'+ str(LeftVar) +'.gif')
    PersonnageVar.goto(PersonnageVar.xcor()-5, PersonnageVar.ycor())
    LeftVar+=1


def Right():
    global RightVar
    global LeftVar
    if int(LeftVar) >= 1:
        LeftVar = 1
    if int(RightVar) > 4:
        RightVar = 1
    turtle.Screen().addshape('img/personnage/WalkRight' + str(RightVar) + '.gif')
    PersonnageVar.shape('img/personnage/WalkRight' + str(RightVar) + '.gif')
    PersonnageVar.goto(PersonnageVar.xcor() + 5, PersonnageVar.ycor())
    RightVar+=1
if __name__ == '__main__':
    personnage(0)
    turtle.mainloop()