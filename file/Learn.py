import pygame as pg
from sys import exit
import random,time
from pygame.locals import *

def game_over():
    font_end = pg.font.Font(None,50)
    game_over_text = font_end.render("Game Over",False,"red")
    game_over_text_rect  = game_over_text.get_rect(center = (WD/2 , HG/2))
    pg.draw.ellipse(Screen,'gray',(WD/2 -100, HG/2-50, 200, 100), 2)
    Screen.blit(game_over_text,game_over_text_rect)

def welcom_text():
    Font = pg.font.Font(None,50)
    welcom_text = Font.render("Welcoe To Mamad Game",False,'red') 
    welcom_rect = welcom_text.get_rect(center = (WD/2,50))
    pg.draw.rect(Screen,'gray',welcom_rect,25)
    pg.draw.rect(Screen,'gray',welcom_rect)
    Screen.blit(welcom_text,welcom_rect)

def main():

    Screen.blit(BG,(0,0))
    Screen.blit(ground,ground_rect_1)
    Screen.blit(Block,Block_surface)
    Screen.blit(caracter,caracter_rect)


    





# ________________________________________________ define variable 
WD = 1024 ; HG = 720
green = (0, 255, 0)
pg.display.init()
pg.display.set_caption("this is first game in Ali's World")
pg.init()
Screen = pg.display.set_mode((WD,HG),pg.RESIZABLE)
Clock = pg.time.Clock()
# Block speed
Block_speed = 4
#carector control
carector_y = HG -142
carector_x = 20
carector_gravity = 0
carector_speed = 10
#Time
Time = time.time()

#  ____________________________________________ image 

ground = (pg.image.load("pic\ground.png").convert())
ground_rect_1 = ground.get_rect(bottomleft= (0,HG + 50))

BG = pg.image.load("pic\milky-way-2695569_1280.jpg").convert()
Block = pg.image.load("pic\mamad_resized.jpg").convert_alpha()
Block_x = WD
Block_surface = Block.get_rect(bottomleft = (Block_x,HG -142))

caracter = pg.image.load("pic\carector.png").convert_alpha()


# _____________________________________
#rtime is real time of game has beeen gone 

while True :
    Clock.tick(50)
    rtime  = time.time() - Time
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                carector_gravity = -20
                carector_gravity +=1
                carector_y += carector_gravity
    
    keys = pg.key.get_pressed()  

    #   har 2 sec be  sorate jabe jay ezafe beshe 
    if rtime>2 and rtime%2 == 0:
        carector_speed = rtime - carector_speed 
        
            
    if keys[pg.K_a]:
        carector_x -=carector_speed
    if keys[pg.K_d]:
        carector_x +=carector_speed

    # mouse_x,mouse_y= pg.mouse.get_pos()

    if carector_y <HG -142 :
        carector_gravity +=1
        carector_y += carector_gravity
          
    elif carector_y <=  HG - 300:
        carector_y = HG - 300
        carector_gravity +=1
        carector_y += carector_gravity

    caracter_rect = caracter.get_rect(midbottom =( carector_x,carector_y))      
    #___________________ Block
    Block_speed += 0.0006
    Block_surface.x -= Block_speed
    if Block_surface.left <= 0 : 
        Block_surface.right = 1024
     
    main()
    x = 0
    #collid
    if caracter_rect.colliderect(Block_surface):
        while x <2:
            main()
            game_over()
            pg.display.update()
            x += 0.001
        exit()
        beeak

    # یه کاری کن که دقتی طرف از رویه کاراکتر رد شد بهش امتیاز بدی



    welcom_text()

    pg.display.update()
