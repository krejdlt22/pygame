# pouzite knihovny
import sys

# pouzity framework
import pygame
# spusteni frameworku
pygame.init()

ROZLISENI = ROZLISENI_X, ROZLISENI_Y = 800, 600

# vytvoreni okna (stanoveni rozliseni)
okno = pygame.display.set_mode(ROZLISENI)

# pocatecni hodnoty
rozmer_x = rozmer_y = 50
pozice_x = 200
pozice_y = 100

# vykreslovaci smycka
while True:
    
    # projdeme si vsechny udale udalosti
    for udalost in pygame.event.get():
        # nastala udalost vypnuti aplikace
        if udalost.type == pygame.QUIT:
            # vypnuti frameworku
            pygame.quit()
            # vypnuti aplikace
            sys.exit()
    
    # zjisteni stavu klavesnice
    klavesnice = pygame.key.get_pressed()
    
    # vypinani aplikace klavesou Escape
    if klavesnice[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    
    # pohyb ctverecku klavesnici
    if klavesnice[pygame.K_LEFT]:
        pozice_x -= 0.1
    if klavesnice[pygame.K_RIGHT]:
        pozice_x += 0.1
    if klavesnice[pygame.K_UP]:
        pozice_y -= 0.1
    if klavesnice[pygame.K_DOWN]:
        pozice_y += 0.1
    
    # omezeni pohybu ctverecku
    if pozice_x < 0:
        pozice_x = 0
    if pozice_y < 0:
        pozice_y = 0
    if pozice_x > ROZLISENI_X - rozmer_x:
        pozice_x = ROZLISENI_X - rozmer_x
    if pozice_y > ROZLISENI_Y - rozmer_y:
        pozice_y = ROZLISENI_Y - rozmer_y
    
    # barva pozadi
    #           R    G    B
    okno.fill((255, 255, 255))
    
    # zobrazeni ctverecku
    #                kde     barva           pozice             rozmery
    pygame.draw.rect(okno, (0, 0, 0), (pozice_x, pozice_y, rozmer_x, rozmer_y))
    
    # refresh zobrazeni
    pygame.display.update()
