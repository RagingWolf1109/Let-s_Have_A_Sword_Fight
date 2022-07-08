import pygame


# when a sprite pallete is created go back to the tutorial to add in attacking again and sprite animations and death/game over

class Fighter:
    def __init__(self,player,x,y):
        self.player = player



        self.flip = False
        self.rect = pygame.Rect((x,y,80,180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100

    def move(self,screen_width,screen_height,surface,target):
        SPEED = 10
        GRAVITY = 2
        dx = 0 
        dy = 0

        #get keypress
        key = pygame.key.get_pressed()

        #Limit what can be done if attacking 
        if self.attacking == False:
            #Player 1 Controls
            if self.player == 1:
                #movement
                if key[pygame.K_a]:
                    dx = -SPEED
                if key[pygame.K_d]: 
                    dx = SPEED
                #jump
                if key[pygame.K_w] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True
                #attack 
                if key[pygame.K_r] or key[pygame.K_t]:
                    #determine which attack was used 
                    self.attack(surface,target)
                    if key[pygame.K_r]:
                        self.attack_type = 1
                    if key[pygame.K_t]:
                        self.attack_type = 2
            #Player 2 Controls
            if self.player == 2:
                #movement
                if key[pygame.K_LEFT]:
                    dx = -SPEED
                if key[pygame.K_RIGHT]: 
                    dx = SPEED
                #jump
                if key[pygame.K_UP] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True
                #attack 
                if key[pygame.K_KP1] or key[pygame.K_KP2]:
                    #determine which attack was used 
                    self.attack(surface,target)
                    if key[pygame.K_KP1]:
                        self.attack_type = 1
                    if key[pygame.K_KP2]:
                        self.attack_type = 2


        #gravity
        self.vel_y += GRAVITY
        dy += self.vel_y
        
        #ensure player stays on screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left 
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 110:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 110 - self.rect.bottom

        #Ensure Players Face Each Other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True
        #update player position
        self.rect.x += dx
        self.rect.y += dy


    def attack(self,surface,target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip),self.rect.y,2*self.rect.width,self.rect.height)
        if attacking_rect.colliderect(target.rect):
            target.health -= 10
        pygame.draw.rect(surface,(0,255,0),attacking_rect)
        

    def draw(self, surface):
        pygame.draw.rect(surface,(255,0,0),self.rect)
