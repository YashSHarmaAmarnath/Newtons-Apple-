# Importing module
import pygame 
from pygame.locals import *
from random import randint
pygame.init
pygame.font.init()

# Window and font
reso = (WIDTH,HEIGHT) = (400,600)
WIN = pygame.display.set_mode(reso)
pygame.display.set_caption("Newton's Apple")  
HEALTH_FONT = pygame.font.SysFont('comicsans', 50)
# Game Constant
FPS = 60
x2=randint(0, WIDTH)
y2=2
player_rect =Rect(200,550,70,90)
food_rect =Rect(10,50,20,20)
speed = 3
step = 0
gravity = 2
score = 0

# loding image
BG = pygame.transform.scale(pygame.image.load("bg.png"), (800,HEIGHT))
tree = pygame.transform.scale(pygame.image.load("tree.PNG"), (450,250))
food = pygame.transform.scale(pygame.image.load("food.PNG"), (20,20))
w0 = pygame.transform.scale(pygame.image.load("walk/walk_!.png"), (50,50))
w0_1 = pygame.transform.scale(pygame.image.load("walk/walk_1.5.png"), (50,50))
w1 = pygame.transform.scale(pygame.image.load("walk/walk_2.png"), (50,50))
w1_1 = pygame.transform.scale(pygame.image.load("walk/walk_2.5.png"), (50,50))
w2 = pygame.transform.scale(pygame.image.load("walk/walk_3.png"), (50,50))
START = pygame.transform.scale(pygame.image.load("gover.png"), reso)

# showing image and controlling movements
def draw(x2,y2):

    global food_rect,step

    WIN.blit(BG, (-WIDTH/2,0))
    WIN.blit(tree, (-50,-50))
    WIN.blit(tree, (-40,0))
    keys_pressed =pygame.key.get_pressed()
    food_rect =Rect(x2,y2,20,20)
    Score_tetx = HEALTH_FONT.render("Score: " + str(score) , 1,(15,0,0))
    WIN.blit(Score_tetx, (50,10))
    WIN.blit(food, (x2,y2))
    
    if keys_pressed[pygame.K_LEFT] and player_rect.x > 0:
        player_rect.x -= speed         
        if step <=20:
            WIN.blit(pygame.transform.flip(w0, True, False), (player_rect.x,player_rect.y))
            step+=1
        elif step>20 and step<=40:
            WIN.blit(pygame.transform.flip(w0_1, True, False), (player_rect.x,player_rect.y))
            step+=1
        elif step>40 and step<=50:
            WIN.blit(pygame.transform.flip(w1, True, False), (player_rect.x,player_rect.y))
            step+=1
        elif step>50 and step<=70:
            WIN.blit(pygame.transform.flip(w1_1, True, False), (player_rect.x,player_rect.y))
            step+=1
        elif step>70 and step<=90:
            WIN.blit(pygame.transform.flip(w2, True, False), (player_rect.x,player_rect.y))
            step+=1
        else:
            step = 0
    
    elif keys_pressed[pygame.K_RIGHT] and player_rect.x < WIDTH - 50 :
        player_rect.x += speed         
        if step <=20:
            WIN.blit(w0, (player_rect.x,player_rect.y))
            step+=1
        elif step>20 and step<=40:
            WIN.blit(w0_1, (player_rect.x,player_rect.y))
            step+=1
        elif step>40 and step<=50:
            WIN.blit(w1, (player_rect.x,player_rect.y))
            step+=1
        elif step>50 and step<=70:
            WIN.blit(w1_1, (player_rect.x,player_rect.y))
            step+=1
        elif step>70 and step<=90:
            WIN.blit(w2, (player_rect.x,player_rect.y))
            step+=1
        else:
            step = 0
    else:
        WIN.blit(w2, (player_rect.x,player_rect.y))
        
#GAem over window
def out():
            print("OUT")            
            clock =pygame.time.Clock()    
            while True:
                for event in pygame.event.get():

                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        pygame.quit()
                    elif event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
                            return
                    elif event.type == pygame.MOUSEBUTTONDOWN :
                        return
                    
                WIN.blit(START, (0,0))    
                pygame.display.update()
                clock.tick(FPS)

# MAin game logic 
def main():
    global y2,x2,player_rect,score,gravity
    clock =pygame.time.Clock()
    run = True
    event = pygame.event.get()
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
           
        if y2>HEIGHT:
            score = 0
            gravity =2
            out()           
        if (y2 > HEIGHT-50 and pygame.Rect.colliderect(player_rect, food_rect)):
            score+=1
            gravity+=0.1
        if y2 > HEIGHT or (y2 > HEIGHT-50 and pygame.Rect.colliderect(player_rect, food_rect)):        
            x2 = randint(0, WIDTH)            
            palyer = pygame.draw.rect(WIN, (225,100,200), food_rect)
            y2 = 0
        y2+=gravity
        draw(x2,y2)
        pygame.display.update()

if __name__ == "__main__":
    main()