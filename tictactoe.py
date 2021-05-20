import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))
x=1
o=2
grid =[
    [0,0,0],
    [0,0,0],
    [0,0,0],
]
pygame.display.set_caption('Tic Tac Toe')

done = False
while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill((255,255,255))
        pygame.display.update()
      

pygame.quit()

