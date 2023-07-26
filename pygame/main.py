
## Built from a youtube tutorial ( Tech with Tim ) : https://www.youtube.com/watch?v=i6xMBig-pP4&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5&pp=iAQB

import pygame

pygame.init()

# create a window 
window_width = 500
window_height = 480
window = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("First Game")

walkRight = [ pygame.image.load('img/R1.png'), pygame.image.load('img/R2.png'), pygame.image.load('img/R3.png'), pygame.image.load('img/R4.png'),
             pygame.image.load('img/R5.png'), pygame.image.load('img/R6.png'), pygame.image.load('img/R7.png'), pygame.image.load('img/R8.png'),
             pygame.image.load('img/R9.png')]
walkLeft = [ pygame.image.load('img/L1.png'), pygame.image.load('img/L2.png'), pygame.image.load('img/L3.png'), pygame.image.load('img/L4.png'),
             pygame.image.load('img/L5.png'), pygame.image.load('img/L6.png'), pygame.image.load('img/L7.png'), pygame.image.load('img/L8.png'),
             pygame.image.load('img/L9.png')]
bg = pygame.image.load('img/bg.jpg')
char = pygame.image.load('img/standing.png')

clock = pygame.time.Clock()

# Sound
bulletSound = pygame.mixer.Sound('bullet.mp3')
hitSound = pygame.mixer.Sound('hit.mp3')

music = pygame.mixer.music.load('img/music.mp3')
#pygame.mixer.music.play(-1)

score = 0

class player():
    def __init__ (self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height 
        self.velocity = 5
        self.isJump = False 
        self.jumpCount  = 10
        self.left = False 
        self.right = False 
        self.walkCount = 0
        self.standing = True 
        self.hitbox = (self.x + 17, self.y+ 11, 29, 52)
        
    
    def draw(self, window):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not (self.standing):
            if self.left:
                window.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                window.blit(walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                window.blit(walkRight[0], (self.x, self.y))
            else:
                window.blit(walkLeft[0], (self.x, self.y))
        
        
        self.hitbox = (self.x + 17, self.y+ 11, 29, 52)
        #pygame.draw.rect(window, (255,0,0), self.hitbox, 2)
    
    def hit(self):
        self.isJump = False 
        self.jumpCount = 10
        self.x = 100
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255,0,0))
        window.blit(text, (250 - ( text.get_width() /2 ), 200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
        pass
    pass

class projectile():
    def __init__(self, x , y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius 
        self.color = color 
        self.facing  = facing
        self.velocity = 8 * facing 
        pass

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)
        pass 
    pass


class enemy(object):
    walkRight = [pygame.image.load('img/R1E.png'), pygame.image.load('img/R2E.png'), pygame.image.load('img/R3E.png'), pygame.image.load('img/R4E.png'),
                 pygame.image.load('img/R5E.png'), pygame.image.load('img/R6E.png'), pygame.image.load('img/R7E.png'), pygame.image.load('img/R8E.png'), 
                 pygame.image.load('img/R9E.png'), pygame.image.load('img/R10E.png'), pygame.image.load('img/R11E.png') ]
    walkLeft = [pygame.image.load('img/L1E.png'), pygame.image.load('img/L2E.png'), pygame.image.load('img/L3E.png'), pygame.image.load('img/L4E.png'),
                 pygame.image.load('img/L5E.png'), pygame.image.load('img/L6E.png'), pygame.image.load('img/L7E.png'), pygame.image.load('img/L8E.png'), 
                 pygame.image.load('img/L9E.png'), pygame.image.load('img/L10E.png'), pygame.image.load('img/L11E.png') ]
    
    def __init__ (self, x , y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height 
        self.end = end 
        self.walkCount = 0
        self.velocity = 3
        self.path = [self.x, self.end]
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True 
        pass

    def draw(self, window):
        self.move()
        if self.visible: 
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            
            if self.velocity > 0:
                window.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                window.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            
            pygame.draw.rect(window, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(window, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            pass

    def move(self):
        if self.velocity > 0:
            if self.x + self.velocity < self.path[1]:
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1 
                self.walkCount = 0
        else:
            if self.x - self.velocity > self.path[0]:
                self.x +=  self.velocity
            else:
                self.velocity = self.velocity * -1
                self.walkCount = 0
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)

        #pygame.draw.rect(window, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        #pygame.draw.rect(window, (0,255,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        #pygame.draw.rect(window, (255,0,0), self.hitbox, 2)
        pass 

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        pass
        
    pass

screenWidth = 500


def redrawGameWindow():
    window.blit(bg, (0,0))
    text = font.render('Score: ' + str(score), 2, (0,0,0))
    window.blit(text, (350, 1))
    man.draw(window)
    goblin.draw(window)
    for bullet in bullets:
        bullet.draw(window)
    pygame.display.update()   

#mainloop
font = pygame.font.SysFont('comicsans', 20, True)
man = player(300, 410, 64, 64)
goblin = enemy(100, 410, 64, 64, 450)
shootLoop = 0
bullets = []
run = True
while run:
    clock.tick(27)

    if goblin.visible == True:
        if man.hitbox[1]  < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0]  < goblin.hitbox[0] + goblin.hitbox[2]:
                man.hit()
                score -= 5
           
    
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                hitSound.play()
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet)) 

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet)) 

    keys = pygame.key.get_pressed()
   
    if keys[pygame.K_SPACE] and shootLoop == 0:
        bulletSound.play()
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width//2), round(man.y + man.height//2), 6, (0,0,0), facing ))
        pass
        shootLoop = 1

    if keys[pygame.K_LEFT] and man.x > man.velocity:
        man.x -= man.velocity
        man.left = True
        man.right = False 
        man.standing = False 
    elif keys[pygame.K_RIGHT] and man.x < screenWidth - man.width - man.velocity:
        man.x += man.velocity
        man.right = True
        man.left = False 
        man.standing = False 
    else:
        man.standing = True
        man.walkCount = 0
    if not (man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False 
            man.left = False 
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1 
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()