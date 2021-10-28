import pygame
import math

pygame.init()

modex, modey = 700, 600
window = pygame.display.set_caption("GAME!!")
window = pygame.display.set_mode((modex, modey))

#setting the font we will use in the game
font = pygame.font.SysFont("comicsansms", 35) 
#setting the x, y coordinates, radius and velocity of the circle
x, y, radius, vel = modex/2, modey, 30, 15 
#setting the colors we will use
green, blue = (0, 255, 0), (0, 0, 128) 
#setting the length and width of the rectangle - it becomes a square since length = width
rectx, recty , rectx1, recty1 = 50, 50, 50, 50
#setting the x-y coordinates and velocity of each square 
rect, rect1 = [700, 600, 1], [0, 500, 1.3]
#Boolean values required for the game-play
run, jump, move_right, move_left, move_right1, move_left1 = True, False, False, True, True, False
#initalizing the clock method in pygame
clock = pygame.time.Clock()


def HasCollided(rx, ry, cx, cy):
    if cx > rx:
        cx -= rectx                           
    distance = math.sqrt((math.pow(rx-cx,2)) + (math.pow(ry-cy,2)))
    if distance < (radius+2):
        return True
    else:
        return False 

while run:
    pygame.time.delay(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and x < modex - radius:
        x += 10
    if keys[pygame.K_LEFT] and x > radius:
        x -= 10 
        #Jump
    if jump is False and keys[pygame.K_UP]:
        jump = True
    if jump is True:
        y -= vel * 2
        vel -= 2
        if vel < -15:
            jump = False
            vel = 15  
    print(y)
    #Moving the square 1
    if move_left is True:
        rect[0] -= rect[2]
        if rect[0] < 0:
            move_left = False
            move_right = True
    if move_right is True:
        rect[0] += rect[2]
        if rect[0] > modex-rectx:
            move_left = True
            move_right = False
    rect[2] += .005
    #Moving the square 2
    if move_left1 is True:
        rect1[0] -= rect1[2]
        if rect1[0] < 0:
            move_left1 = False
            move_right1 = True
    if move_right1 is True:
        rect1[0] += rect1[2]
        if rect1[0] > modex-rectx1:
            move_left1 = True
            move_right1 = False 
    rect1[2] += .005

    window.fill ((25, 30, 100))
    pygame.draw.circle(window, (0, 0, 0), (int(x), int(y - radius)), radius)
    pygame.draw.rect(window, (255, 0, 0), (rect[0], rect[1]-recty, rectx, recty))
    pygame.draw.rect(window, (20, 100, 0), (rect1[0], rect1[1]-recty, rectx, recty))
    pygame.display.update()
    
    Collision = HasCollided(rect[0], rect[1], x, y)  
    if Collision == True:
        text = font.render('Game Over', True, green)
        window.blit(text, [300, modey/2])
        pygame.display.update()
        pygame.time.delay(1000)
        run = False
    Collision1 = HasCollided(rect1[0], rect1[1], x, y)  
    if Collision1 == True:
        text = font.render('Game Over', True, green)
        window.blit(text, [300, modey/2])
        pygame.display.update()
        pygame.time.delay(1000)
        run = False

pygame.quit()