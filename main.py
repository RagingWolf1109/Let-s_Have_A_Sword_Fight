import pygame
from fighter import Fighter

pygame.init()

#Create the Game Window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Let's Have A Sword Fight")

#Set Frame Rate
clock = pygame.time.Clock()
FPS = 60

#Define Colors
YELLOW = (255,255,0)
RED = (255,0,0)
WHITE = (255,255,255)

#Load Background Image
bg_image = pygame.image.load("assets/level1.png").convert_alpha() # why convert_alpha?

#Function for Drawing Background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.blit(scaled_bg,(0,0))
#Function for Drawing Health
def draw_health_bar(health,x,y):
    ratio = health / 100
    pygame.draw.rect(screen,WHITE,(x-1,y-1,404,34))
    pygame.draw.rect(screen,RED,(x,y,400,30))
    pygame.draw.rect(screen, YELLOW,(x,y,400*ratio,30))

#create two instances of fighter
fighter_1 = Fighter(1,200,310)
fighter_2 = Fighter(2,700,310)



#game loop
run = True
while run:

    clock.tick(FPS)

    #Draw background
    draw_bg()
    #Show Health Bars
    draw_health_bar(fighter_1.health,20,20)
    draw_health_bar(fighter_2.health,500,20)
    #Draw Fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)
    #Move Fighters
    fighter_1.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter_2)
    fighter_2.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter_1)


    #Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    #Update Screen
    pygame.display.update()


#Exit Pygame
pygame.quit()