# pouzite knihovny
import sys

# pouzity framework
import pygame
# spusteni frameworku
pygame.init()

# vytvoreni okna (stanoveni rozliseni)
okno = pygame.display.set_mode((800, 600))

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
    
    # barva pozadi
    #           R    G    B
    okno.fill((255, 255, 255))
    
    # zobrazeni ctverecku
    #                kde     barva      pozice   rozmery
    pygame.draw.rect(okno, (0, 0, 0), (200, 100, 50, 50))
    
    # refresh zobrazeni
    pygame.display.update()
