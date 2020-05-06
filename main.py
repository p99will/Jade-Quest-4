 # Imports
import os,sys,time,random

import pygame
from pygame.locals import *
# End of Imports

# Globals
FPS = 60
WINDOW_TITLE = "Jade Quest 4 In-Dev"
DEBUG = True

display = None
glob = None
fpsClock = None
# End of Globals

# Classes
class colors:
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)

class game():
    sprites=[]
    sprit_count=0
    player=None

    def new_sprite(self):
        uid = self.sprit_count
        self.sprit_count += 1
        return uid

class sprite():
    id=None
    x=0
    y=0
    width=0
    height=0
    visible=True
    tags=[]
    name=""

    def __init__(self,name='',x=0,y=0,width=0,height=0,tags=[],visible=True):
        self.id = glob.new_sprite()
        if name == '':
            name = "Sprite" + str(self.id)
        self.name=name
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.tags=tags
        self.visible=visible
        log("Made Sprite: '" + name + "' with ID: " + str(self.id))

    def draw(self):
        pass

    def tick(self):
        pass

class shape(sprite):
    thickness=0
    color=0

    def __init__(self,name='',x=0,y=0,width=0,height=0,thickness=0,color=colors.white,
            tags=[], visible=True):
        sprite.__init__(self,name,x,y,width,height,tags,visible)
        self.thickness=thickness
        self.color=color

    def draw(self):
        pygame.draw.rect(display, self.color, (self.x,self.y,
            self.width,self.height),self.thickness)

    def tick(self):
        pass

class player(shape):
    speed=5
    vol=[0,0]
    def tick(self):
        self.x += self.speed * self.vol[0]
        self.y += self.speed * self.vol[1]
# end of Classes

# Methods
def log(text):
    if DEBUG:
        print("DEBUG: " + text)

def setup():
    print(WINDOW_TITLE)

    glob.sprites.append(shape("frame",2,2,500,500,2,colors.blue))
    glob.player=player("player",50,50,25,25,0,colors.green)

    for i in range(10):
        x=random.randint(0,400)
        y=random.randint(0,400)
        glob.sprites.append(shape("wall",x,y,50,50,0,colors.white,"wall"))

def check_key_press(key,press):
    if key == "left":
        glob.player.vol[0] = -1 * press
    if key == "right":
        glob.player.vol[0] = 1 * press
    if key == "up":
        glob.player.vol[1] = -1 * press
    if key == "down":
        glob.player.vol[1] = 1 * press


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        keys = pygame.key.get_pressed()

        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            log("key press: " + key)
            check_key_press(key,1)

        if event.type == pygame.KEYUP:
            key = pygame.key.name(event.key)
            log("key release: " + key)
            check_key_press(key,0)

def game_tick():
    glob.player.tick()

    draw_things()
    pygame.display.update()
    fpsClock.tick(FPS)

def draw_things():
    display.fill(colors.black)
    for i in glob.sprites:
        i.tick()
        i.draw()

    glob.player.draw()
# End of Methods



# Initiation
pygame.init()
pygame.font.init()

fpsClock = pygame.time.Clock()
display = pygame.display.set_mode((800,600))
glob = game()

setup()

# End of Initiation

# Main loop
while True:
    check_events()
    game_tick()
