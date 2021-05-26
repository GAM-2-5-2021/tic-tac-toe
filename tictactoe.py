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

icon=pygame.image.load('icon.png') 
pygame.display.set_icon(icon)

done = False
while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill((255,255,255))
        font = pygame.font.SysFont('Arial', 20)
        text = font.render('Križić-Kružić', True, (0,0,0), (255,255,255))
        textRect = text.get_rect()
        textRect.center = (250, 150)
        screen.fill((255, 255, 255))
        screen.blit(text, textRect)
        #screen.fill((255,255,255))      
        #pygame.draw.line(screen, (0,0,0), (500 / 3, 0), (500 / 3, 500), 5) 
        #pygame.draw.line(screen, (0,0,0), (500 / 3 * 2, 0), (500 / 3 * 2, 500), 5)
        #pygame.draw.line(screen, (0,0,0), (0, 500 / 3), (500, 500 / 3), 5) 
        #pygame.draw.line(screen, (0,0,0), (0, 500 / 3 * 2), (500, 500 / 3 * 2), 5)
        pygame.display.update()
      
pygame.quit()
