import pygame

WindowWidth = 400
WindowHeight = 500
FPS = 30

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WindowWidth,WindowHeight))
pygame.display.set_caption("My first Game")
clock = pygame.time.Clock()

running = True

while(running):
    #clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.draw.rect(screen, (0, 150, 0), [200, 250, 20, 20])
    pygame.display.update()

    


pygame.quit()
