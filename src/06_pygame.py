# pouzite knihovny
import sys
# pouzity framework
import pygame
# spusteni frameworku
pygame.init()

# pocatecni hodnoty
ROZLISENI = ROZLISENI_X, ROZLISENI_Y = 800, 600
FPS_COUNT = 60

rozmer_x = rozmer_y = 50
pozice_x = (ROZLISENI_X - rozmer_x) / 2
pozice_y = (ROZLISENI_Y - rozmer_y) / 2
rychlost = 3 # pixely / frame

# nacteni textury
logo = pygame.image.load('../data/logo.png')
textura = pygame.transform.scale(logo, (rozmer_x, rozmer_y))

# vytvoreni okna (stanoveni rozliseni)
okno = pygame.display.set_mode(ROZLISENI)
pygame.display.set_caption('SPŠ Hide & Seek')
pygame.display.set_icon(logo)

# pomocny objekt pro nastaveni FPS
hodiny = pygame.time.Clock()

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
        pozice_x -= rychlost
    if klavesnice[pygame.K_RIGHT]:
        pozice_x += rychlost
    if klavesnice[pygame.K_UP]:
        pozice_y -= rychlost
    if klavesnice[pygame.K_DOWN]:
        pozice_y += rychlost
    
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
    
    # zobrazeni textur na pozadi
    for x in range(0, ROZLISENI_X, rozmer_x):
        for y in range(0, ROZLISENI_Y, rozmer_y):
            okno.blit(textura, (x, y))
    else:
        # zobrazeni pohyblive textury na popredi
        okno.blit(textura, (pozice_x, pozice_y))
    
    # refresh zobrazeni
    pygame.display.update()
    # nastaveni max. poctu snimku za sekundu
    hodiny.tick(FPS_COUNT)

