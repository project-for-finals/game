import pygame

WindowWidth = 600
WindowHeight = 500
FPS = 30

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WindowWidth,WindowHeight))
pygame.display.set_caption("My first Game")
clock = pygame.time.Clock()


pad_y = 100
pad_dy = 0.2
press = 0.2


running = True
while(running):
    #clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pad_dy *= -1
            '''elif event.key == pygame.K_DOWN:
                pad_dy = 0.2'''
    pad_y += pad_dy


    if pad_y > WindowHeight - 40 or pad_y < 20:
        pad_dy *= -1

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 150, 0), [200, pad_y, 20, 20])
    pygame.draw.rect(screen, (150, 150, 0), [0, 0, 600, 20])
    pygame.draw.rect(screen, (150, 150, 0), [0, 480, 600, 20])
    pygame.display.update()


pygame.quit()
