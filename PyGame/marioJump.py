import pygame
pygame.init()

win = pygame.display.set_mode((1000,500))
pygame.display.set_caption("First Game")

x = 50
y = 350
width = 40
height = 60
vel = 10

isJump = False
jumpCount = 10

run = True

clock = pygame.time.Clock()

while run:
    pygame.time.delay(5)
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and x > vel: 
        x -= vel

    if keys[pygame.K_d] and x < 1000 - vel - width:  
        x += vel
        
    if not(isJump): 
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= (jumpCount ** 3) * 0.05
            if jumpCount >= 2:
                pygame.time.delay(5)
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False
    
    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))   
    pygame.display.update() 
    
pygame.quit()