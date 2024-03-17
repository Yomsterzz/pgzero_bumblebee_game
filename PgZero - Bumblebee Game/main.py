import pgzrun
from random import randint

WIDTH = 512
HEIGHT = 480

bee = Actor("bee")
bee.pos = 256,256

flower = Actor("flower")
flower.pos = 50,50

score = 0
isgameover = False

def draw():
    screen.blit("background", (0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score: " + str(score), color='black', topleft=(10,10))
    if isgameover:
        screen.fill("teal")
        screen.draw.text("Game Over. You scored {} points.".format(score), color="green", midtop=(WIDTH/2, HEIGHT/2), fontsize=30)

def move_flower():
    prevx = 200
    prevy = 200
    x = randint(70,WIDTH-70)
    y = randint(70,HEIGHT-70)
    if (x + prevx/2) < WIDTH-70:
        flower.x = x + prevx/2
        prevx = x
    else:
        flower.x = x
        prevx = x
    if (y + prevy/2) < WIDTH-70:
        flower.y = y + prevy/2
        prevx = y
    else:
        flower.y = y
        prevx = y


def gameover():
    global isgameover
    isgameover = True

def update():
    global score
    if keyboard.left:
        bee.x -= 5
    if keyboard.right:
        bee.x += 5
    if keyboard.down:
        bee.y += 5
    if keyboard.up:
        bee.y -= 5
    iscollided = bee.colliderect(flower)
    if iscollided:
        score += 10
        move_flower()

clock.schedule(gameover, 20)


pgzrun.go()