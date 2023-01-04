# pouzity framework
import pygame
# spusteni frameworku
pygame.init()

# vytvoreni okna (stanoveni rozliseni)
okno = pygame.display.set_mode((800, 600))

# barva pozadi
#           R    G    B
okno.fill((255, 255, 255))

# refresh zobrazeni
pygame.display.update()
