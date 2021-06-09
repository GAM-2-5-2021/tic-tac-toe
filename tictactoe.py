import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption('Tic-Tac-Toe')

icon=pygame.image.load('icon.png') 
pygame.display.set_icon(icon)

oblik = 'o'

linija1= pygame.draw.rect(screen, (0, 0, 0), (160, 0, 10, 500)) 
linija2 = pygame.draw.rect(screen, (0, 0, 0), (330, 0, 10, 500))
linija3 = pygame.draw.rect(screen, (0, 0, 0), (0, 160, 500, 10))
linija4 = pygame.draw.rect(screen, (0, 0, 0), (0, 330, 500, 10))

prvo_polje = pygame.draw.rect(screen, (255, 255, 255), (0, 0, 160, 160))
drugo_polje = pygame.draw.rect(screen, (255, 255, 255), (170, 0, 160, 160))
trece_polje = pygame.draw.rect(screen, (255, 255, 255), (340, 0, 160, 160))
cetvrto_polje = pygame.draw.rect(screen, (255, 255, 255), (0, 170, 160, 160))
peto_polje = pygame.draw.rect(screen, (255, 255, 255), (170, 170, 160, 160))
sesto_polje = pygame.draw.rect(screen, (255, 255, 255), (340, 170, 160, 160))
sedmo_polje = pygame.draw.rect(screen, (255, 255, 255), (0, 340, 160, 160))
osmo_polje = pygame.draw.rect(screen, (255, 255, 255), (170, 340, 160, 160))
deveto_polje = pygame.draw.rect(screen, (255, 255, 255), (340, 340, 160, 160))

prvo_slobodno = True
drugo_slobodno = True
trece_slobodno = True
cetvrto_slobodno = True
peto_slobodno = True
sesto_slobodno = True
sedmo_slobodno = True
osmo_slobodno = True
deveto_slobodno = True

run = True
while run:   
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                prvo_slobodno = True
                drugo_slobodno = True
                trece_slobodno = True
                cetvrto_slobodno = True
                peto_slobodno = True
                sesto_slobodno = True
                sedmo_slobodno = True
                osmo_slobodno = True
                deveto_slobodno = True
                run = True
                linija1= pygame.draw.rect(screen, (0, 0, 0), (160, 0, 10, 500)) 
                linija2 = pygame.draw.rect(screen, (0, 0, 0), (330, 0, 10, 500))
                linija3 = pygame.draw.rect(screen, (0, 0, 0), (0, 160, 500, 10))
                linija4 = pygame.draw.rect(screen, (0, 0, 0), (0, 330, 500, 10))
                prvo_polje = pygame.draw.rect(screen, (255, 255, 255), (0, 0, 160, 160))
                drugo_polje = pygame.draw.rect(screen, (255, 255, 255), (170, 0, 160, 160))
                trece_polje = pygame.draw.rect(screen, (255, 255, 255), (340, 0, 160, 160))
                cetvrto_polje = pygame.draw.rect(screen, (255, 255, 255), (0, 170, 160, 160))
                peto_polje = pygame.draw.rect(screen, (255, 255, 255), (170, 170, 160, 160))
                sesto_polje = pygame.draw.rect(screen, (255, 255, 255), (340, 170, 160, 160))
                sedmo_polje = pygame.draw.rect(screen, (255, 255, 255), (0, 340, 160, 160))
                osmo_polje = pygame.draw.rect(screen, (255, 255, 255), (170, 340, 160, 160))
                deveto_polje = pygame.draw.rect(screen, (255, 255, 255), (340, 340, 160, 160))
    #screen.fill((255,255,255))
    #font = pygame.font.SysFont('Arial', 20)
    #text = font.render('Križić-Kružić', True, (0, 0, 0), (255, 255, 255))
    #textRect = text.get_rect()
    #textRect.center = (250, 100)
    #screen.fill((255, 255, 255))
    #screen.blit(text, textRect)

    if event.type == pygame.MOUSEBUTTONUP:
            pozicija = pygame.mouse.get_pos()

            if prvo_polje.collidepoint(pozicija) and prvo_slobodno:
                if oblik == 'o':
                    pygame.draw.circle(screen,(255, 0, 0), (80, 80), 50)
                    pygame.draw.circle(screen,(255, 255, 255), (80, 80), 45)
                    oblik = 'x'
                else:
                    pygame.draw.line(screen, (0, 0, 255), (30, 30), (130, 130))
                    pygame.draw.line(screen, (0, 0, 255), (130, 30), (30, 130))
                    oblik = 'o'
                prvo_slobodno = False
                    
            if drugo_polje.collidepoint(pozicija) and drugo_slobodno:
                if oblik == 'o':
                    pygame.draw.circle(screen,(255, 0, 0), (250, 80), 50)
                    pygame.draw.circle(screen,(255, 255, 255), (250, 80), 45)
                    oblik = 'x'
                else:
                    pygame.draw.line(screen, (0, 0, 255), (200, 30), (300, 130))
                    pygame.draw.line(screen, (0, 0, 255), (300, 30), (200, 130))
                    oblik = 'o'
                drugo_slobodno = False
                    
            if trece_polje.collidepoint(pozicija) and trece_slobodno:
                if oblik == 'o':
                    pygame.draw.circle(screen,(255, 0, 0), (420, 80), 50)
                    pygame.draw.circle(screen,(255, 255, 255), (420, 80), 45)
                    oblik = 'x'
                else:
                    pygame.draw.line(screen, (0, 0, 255), (370, 30), (470, 130))
                    pygame.draw.line(screen, (0, 0, 255), (470, 30), (370, 130))
                    oblik = 'o'
                trece_slobodno = False
                    
            if cetvrto_polje.collidepoint(pozicija) and cetvrto_slobodno:
                if oblik == 'o':
                    pygame.draw.circle(screen,(255, 0, 0), (80, 250), 50)
                    pygame.draw.circle(screen,(255, 255, 255), (80, 250), 45)
                    oblik = 'x'
                else:
                    pygame.draw.line(screen, (0, 0, 255), (30, 200), (130, 300))
                    pygame.draw.line(screen, (0, 0, 255), (130, 200), (30, 300))
                    oblik = 'o'
                cetvrto_slobodno = False
                    
            if peto_polje.collidepoint(pozicija) and peto_slobodno:
                if oblik == 'o':
                    pygame.draw.circle(screen,(255, 0, 0), (250, 250), 50)
                    pygame.draw.circle(screen,(255, 255, 255), (250, 250), 45)
                    oblik = 'x'
                else:
                    pygame.draw.line(screen, (0, 0, 255), (200, 200), (300, 300))
                    pygame.draw.line(screen, (0, 0, 255), (300, 200), (200, 300))
                    oblik = 'o'
                peto_slobodno = False
                    
            if sesto_polje.collidepoint(pozicija) and sesto_slobodno:
                if oblik == 'o':
                    pygame.draw.circle(screen, (255, 0, 0), (420, 250), 50)
                    pygame.draw.circle(screen, (255, 255, 255), (420, 250), 45)
                    oblik = 'x'
                else:
                    pygame.draw.line(screen, (0, 0, 255), (370, 200), (470, 300))
                    pygame.draw.line(screen, (0, 0, 255), (470, 200), (370, 300))
                    oblik = 'o'
                sesto_slobodno = False
                    
            if sedmo_polje.collidepoint(pozicija) and sedmo_slobodno:
                if oblik == 'o':
                    pygame.draw.circle(screen,(255, 0, 0), (80, 420), 50)
                    pygame.draw.circle(screen,(255, 255, 255), (80, 420), 45)
                    oblik = 'x'
                else:
                    pygame.draw.line(screen, (0, 0, 255), (30, 370), (130, 470))
                    pygame.draw.line(screen, (0, 0, 255), (130, 370), (30, 470))
                    oblik = 'o'
                sedmo_slobodno = False
                    
            if osmo_polje.collidepoint(pozicija) and osmo_slobodno:
                if oblik == 'o':
                    pygame.draw.circle(screen, (255, 0, 0), (250, 420), 50)
                    pygame.draw.circle(screen, (255, 255, 255), (250, 420), 45)
                    oblik = 'x'
                else:
                    pygame.draw.line(screen, (0, 0, 255), (200, 370), (300, 470))
                    pygame.draw.line(screen, (0, 0, 255), (300, 370), (200, 470))
                    oblik = 'o'
                osmo_slobodno = False
                    
            if deveto_polje.collidepoint(pozicija) and deveto_slobodno:
                if oblik == 'o':
                    pygame.draw.circle(screen,(255, 0, 0), (420, 420), 50)
                    pygame.draw.circle(screen,(255, 255, 255), (420, 420), 45)
                    oblik = 'x'
                else:
                    pygame.draw.line(screen, (0, 0, 255), (370, 370), (470, 470))
                    pygame.draw.line(screen, (0, 0, 255), (470, 370), (370, 470))
                    oblik = 'o'
                deveto_slobodno = False

    pygame.display.update()
      
pygame.quit()


