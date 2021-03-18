from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets: #Mueve los globos .5 unidades en X cada refresh
        target.x -= 0.5

    if inside(ball): #Hace que la bola avance cada vez más lento en y
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy() #crea una copia de los globos
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target): #Si no se encuentra dentro de los limites, regresa el globo a X-200 y a una Y aleatoria
            target.x = 200
            target.y = randrange(-150, 150)


    ontimer(move, 15) #Llama la función move cada 15 milisegundos

setup(420, 420, 370, 0)
hideturtle() #Esconde el cursor de turtle
up()
tracer(False)
onscreenclick(tap)
move()
done()