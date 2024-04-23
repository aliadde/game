import pygame as pg
from sys import exit
import random,time
from pygame.locals import *
WD = 1024 ; HG = 720
green = (0, 255, 0)
pg.display.init()
pg.display.set_caption("this is first game in Ali's World")
pg.init()
Screen = pg.display.set_mode((WD,HG),pg.RESIZABLE)
Clock = pg.time.Clock()

#  ____________________________________________

ground = (pg.image.load("ground.png").convert())
ground_rect_1 = ground.get_rect(bottomleft= (0,HG + 50))


# _______________________________
BG = pg.image.load("milky-way-2695569_1280.jpg").convert()
# ________________________________________________
Block_x = WD
Block = pg.image.load("mamad.jpg").convert_alpha()
Block_surface = Block.get_rect(bottomleft = (Block_x,HG -142))
Block_speed = 0
# ______________________________________|

Font = pg.font.Font(None,30)
font_end = pg.font.Font(None,50)

welcom_text = Font.render("Welcoe To Mamad Game",False,(4,200,0)) 
welcom_rect = welcom_text.get_rect(center = (WD/2,50))
game_over_text = font_end.render("Game Over",False,"red")
# _____________________________________
caracter = pg.image.load("carector.png").convert_alpha()
carector_y = HG -142
140 <carector_y <300
Time = time.time()
real_time = 0
 
#_____________
#graity 
carector_gravity = 0


while True :
    Clock.tick(50)


    for event in pg.event.get():
        if event.type == pg.QUIT:
                pg.quit()
                exit()
   

        if  event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                        carector_gravity = -50
                        carector_gravity +=1
                        carector_y += carector_gravity
                     
 
   
    mouse_x,mouse_y= pg.mouse.get_pos()
    if carector_y <HG -142 :
        carector_gravity +=1
        carector_y += carector_gravity
    caracter_rect = caracter.get_rect(midbottom =( mouse_x,carector_y))            

    if carector_y <= 150 :
        carector_y = 150
        carector_gravity +=1
        carector_y += carector_gravity

            





        
        
    #___________________ Block
    Block_speed += 0.06
    Block_surface.x -= Block_speed
    if Block_surface.left <= 0 : 
        Block_surface.right = 1024

    #__________________ Block        



    Screen.blit(BG,(0,0))
    Screen.blit(ground,ground_rect_1)
    Screen.blit(Block,Block_surface)
    Screen.blit(caracter,caracter_rect)
        
    pg.draw.rect(Screen,'gray',welcom_rect,25)
    pg.draw.rect(Screen,'gray',welcom_rect)
        #     pg.draw.ellipse(Screen,'red',pg.Rect(400,50,100,90))
    Screen.blit(welcom_text,welcom_rect)
   
  
    
    pg.display.update()
