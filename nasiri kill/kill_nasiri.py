# header files
import pygame as pg
from sys import exit
from  pygame import locals
#_______________________________________________________________________________________
wd, hg = 1200, 750






run = True
while run:
    pg.init()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            exit()
    
    screen = pg.display.set_mode((wd,hg))

    