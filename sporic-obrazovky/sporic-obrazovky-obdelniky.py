import pygame
import random

pygame.init()

win = pygame.display.set_mode((1440, 900), pygame.FULLSCREEN)
pygame.display.set_caption("Screen saver")

pocitadloCyklu = 0;

# Hlavni herni cyklus
hraBezi = True
while hraBezi:
    # Cyklus pro zachytavani udalosti
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hraBezi = False

    # Ukonceni pomoci klavesy ESC
    stisknuteKlavesy = pygame.key.get_pressed()
    if stisknuteKlavesy[pygame.K_ESCAPE]:
        hraBezi = False

    # Pocitani pruchodu cyklem
    pocitadloCyklu = pocitadloCyklu + 1
    if pocitadloCyklu > 200:
        # Resetovani pocitadla
        pocitadloCyklu = 1
        # Vycisteni obrazovku (nakresleni cerneho obdelniku pres celou obrazovku)
        pygame.draw.rect(win, (0,0,0), (0, 0, 1440, 900))

    # Nahodne generovani barvy
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    nahodnaBarva = (red, green, blue)

    # Nahodne generovani souradnice obdelniku
    x = random.randint(0, 1340)
    y = random.randint(0, 800)

    # Nahodne generovani velikost obdelniku
    sirka = random.randint(10, 100)
    vyska = random.randint(10, 100)

    # Vykresleni nahodneho obdelniku
    pygame.draw.rect(win, nahodnaBarva, (x,y, sirka, vyska))

    # Pockani
    pygame.time.wait(50)

    # Prekresleni / refresh obrazovky
    pygame.display.update()

pygame.quit()