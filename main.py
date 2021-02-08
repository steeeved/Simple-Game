import pygame
import random

pygame.init()


window = pygame.display.set_caption("Simple Game")
window = pygame.display.set_mode((500, 500))
font = pygame.font.Font('freesansbold.ttf', 32)

radius = 30
x = 250
y = 500 
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
rect_x = 420
rect_y = 460
vel_x = 10
vel_y = 10
vel_enemy = 4
jump = False
enemy_spawn = True

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

    if enemy_spawn is True:
        rect_x -= vel_enemy
        #vel_enemy += 0.5
        if rect_x < 20:
            rect_x = random.randint(490, 500)

    if rect_x == x + radius and y-40 == rect_y:
        enemy_spawn = False
        text = font.render('Game Over Bitch!', True, green, blue)
        pygame.display.update()


    window.fill ((0,0,0))
    pygame.draw.circle(window, (255, 0, 0), (int(x), int(y - radius)), radius)
    pygame.draw.rect(window, (0, 0, 255), (rect_x, rect_y, 42, 42))
    pygame.display.update()
    
pygame.quit()