  Collision = HasCollided(rect[0], rect[1], x, y)  
    if Collision == True:
        text = font.render('Game Over Bitch!', True, green)
        window.blit(text, [300, modey/2])
        pygame.display.update()
        pygame.time.delay(1000)
        run = False
    Collision1 = HasCollided(rect1[0], rect1[1], x, y)  
    if Collision1 == True:
        text = font.render('Game Over Bitch!', True, green)
        window.blit(text, [300, modey/2])
        pygame.display.update()
        pygame.time.delay(1000)
        run = False