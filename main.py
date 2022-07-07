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

#Load Background Image
bg_image = pygame.image.load("assets/level1.png").convert_alpha() # why convert_alpha?

#Function for Drawing Background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.blit(scaled_bg,(0,0))

#create two instances of fighter
fighter_1 = Fighter(200,310)
fighter_2 = Fighter(700,310)



#game loop
run = True
while run:

    clock.tick(FPS)

    #Draw background
    draw_bg()
    #Draw Fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)
    #Move Fighters
    fighter_1.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter_2)
    #fighter_2.move(SCREEN_WIDTH)


    #Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    #Update Screen
    pygame.display.update()


#Exit Pygame
pygame.quit()