import pygame

pygame.init()


window = pygame.display.set_caption("Anslem")
window = pygame.display.set_mode((500, 500))

radius = 30
x = 250
y = 500 
vel_x = 10
vel_y = 10
jump = False


run = True
while run:
    pygame.time.delay(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #keys
    keys = pygame.key.get_pressed()
    
   
    if keys[pygame.K_RIGHT] and x < 500 - radius:
        x += vel_x
    if keys[pygame.K_LEFT] and x > 0 + radius:
        x -= vel_x
    if jump is False and keys[pygame.K_UP]:
        jump = True

    if jump is True:
        y -= vel_y * 4
        vel_y -= 1
        if vel_y < -10:
            jump = False
            vel_y = 10


    window.fill ((0,255,0))
    pygame.draw.circle(window, (255, 0, 0), (int(x), int(y - radius)), radius)
    pygame.display.update()
    
pygame.quit()