# pouzite knihovny
import sys

# pouzity framework
import pygame
# spusteni frameworku
pygame.init()

# vytvoreni okna (stanoveni rozliseni)
okno = pygame.display.set_mode((800, 600))

# pocatecni hodnoty
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
    
    # pohyb ctverecku
    pozice_x += 0.1
    pozice_y += 0.1
    
    # barva pozadi
    #           R    G    B
    okno.fill((255, 255, 255))
    
    # zobrazeni ctverecku
    #                kde     barva           pozice        rozmery
    pygame.draw.rect(okno, (0, 0, 0), (pozice_x, pozice_y, 50, 50))
    
    # refresh zobrazeni
    pygame.display.update()
