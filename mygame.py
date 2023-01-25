import sys
import pygame
pygame.init()

ROZLISENI = ROZLISENI_X, ROZLISENI_Y = 1200, 800
FPS_COUNT = 60
rozmer_x = rozmer_y = 50
pozice_x = (ROZLISENI_X - rozmer_x) / 2
pozice_y = (ROZLISENI_Y - rozmer_y) / 2
rychlost = 5
hodiny = pygame.time.Clock()
okno = pygame.display.set_mode(ROZLISENI)

ctverecek_r = 1
ctverecek_g = 1
ctverecek_b = 1
ctverecek_alpha = 254


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

    # blbosti xD
    if klavesnice[pygame.K_q]:
        ctverecek_r += 1
        if ctverecek_r == 255:
            ctverecek_r = 254
    if klavesnice[pygame.K_a]:
        ctverecek_r -= 1
        if ctverecek_r == 0:
            ctverecek_r = 1

    if klavesnice[pygame.K_w]:
        ctverecek_g += 1
        if ctverecek_g == 255:
            ctverecek_g = 254
    if klavesnice[pygame.K_s]:
        ctverecek_g -= 1
        if ctverecek_g == 0:
            ctverecek_g = 1

    if klavesnice[pygame.K_e]:
        ctverecek_b += 1
        if ctverecek_b == 255:
            ctverecek_b = 254
    if klavesnice[pygame.K_d]:
        ctverecek_b -= 1
        if ctverecek_b == 0:
            ctverecek_b = 1

    if klavesnice[pygame.K_r]:
        ctverecek_alpha += 1
        if ctverecek_alpha == 255:
            ctverecek_alpha = 254
    if klavesnice[pygame.K_f]:
        ctverecek_alpha -= 1
        if ctverecek_alpha == 0:
            ctverecek_alpha = 1
    
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
    #           R    G    Bf

    plocha = okno.fill((127,127,127))
    # zobrazeni ctverecku
    #                kde     barva           pozice             rozmery
    ctverecek = pygame.draw.rect(okno, (ctverecek_r, ctverecek_g, ctverecek_b), (pozice_x, pozice_y, rozmer_x, rozmer_y))

    # refresh zobrazeni
    pygame.display.update()
    # nastaveni max. poctu snimku za sekundu
    hodiny.tick(FPS_COUNT)