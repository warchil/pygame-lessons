import pygame

# Pripraveni pygame (inicializace)
pygame.init()

# Vytvoreni herniho okna o dane sirce a vysce
win = pygame.display.set_mode((852, 480))
# Pojmenovani herniho okna
pygame.display.set_caption("Animace goblina")

# Nacteni snimku animace pro cekani (goblin nic nedela a postava na miste)
poleSnimkuCekani = [
    pygame.image.load('goblin/01-Idle_/01-NoBlink/2D_GOBLIN__Idle_000.png'),
    pygame.image.load('goblin/01-Idle_/01-NoBlink/2D_GOBLIN__Idle_001.png'),
    pygame.image.load('goblin/01-Idle_/01-NoBlink/2D_GOBLIN__Idle_002.png'),
    pygame.image.load('goblin/01-Idle_/01-NoBlink/2D_GOBLIN__Idle_003.png'),
    pygame.image.load('goblin/01-Idle_/01-NoBlink/2D_GOBLIN__Idle_004.png'),
    pygame.image.load('goblin/01-Idle_/01-NoBlink/2D_GOBLIN__Idle_005.png'),
    pygame.image.load('goblin/01-Idle_/01-NoBlink/2D_GOBLIN__Idle_006.png'),
    pygame.image.load('goblin/01-Idle_/01-NoBlink/2D_GOBLIN__Idle_007.png'),
]

# Nacteni snimku animace utoku (goblin sekne sekerou)
poleSnimkuUtoku = [
    pygame.image.load('goblin/03-Attack_/2D_GOBLIN__Attack_000.png'),
    pygame.image.load('goblin/03-Attack_/2D_GOBLIN__Attack_001.png'),
    pygame.image.load('goblin/03-Attack_/2D_GOBLIN__Attack_002.png'),
    pygame.image.load('goblin/03-Attack_/2D_GOBLIN__Attack_003.png'),
    pygame.image.load('goblin/03-Attack_/2D_GOBLIN__Attack_004.png'),
    pygame.image.load('goblin/03-Attack_/2D_GOBLIN__Attack_005.png'),
    pygame.image.load('goblin/03-Attack_/2D_GOBLIN__Attack_006.png'),
    pygame.image.load('goblin/03-Attack_/2D_GOBLIN__Attack_007.png'),
]

# Nacteni obrazku pozadi
obrazekPozadi = pygame.image.load('pozadi/bg.jpg')

# Ridici promenne
posledniPrekresleni = pygame.time.get_ticks()
casMeziFramy = 100
cisloFramu = 0

goblinUtoci = False
cisloFramuUtoku = 0

# Promenna "hraBezi" je nastavena na True (Pravda), pokud hra bezi. Jakmile hrac klikne na krizek,
# tak se promenna nastavi na False (Nepravda), hlavni herni cyklus se ukonci a hra konci.
hraBezi = True
# Hlavni herni cyklus
while hraBezi:

    # Cyklus, ktery zjistuje, jake nastaly udalosti.
    for event in pygame.event.get():
        # Pokud hrac kliknul na krizek, tak se nastavi promenna "hraBezi" na False (Nepravda)
        if event.type == pygame.QUIT:
            hraBezi = False

    # Uloz do promenne "aktualniCas" aktualni cas v milisekundach (cislo)
    aktualniCas = pygame.time.get_ticks()

    # Zjisti, jake klavesy byly stisknute a uloz je do promenne "zmacknuteKlavesy"
    zmacknuteKlavesy = pygame.key.get_pressed()

    # Pokud byla stisknuta klavesa mezernik, tak nastavi promennou "goblinUtoci" na True (Pravda)
    if zmacknuteKlavesy[pygame.K_SPACE]:
        goblinUtoci = True

    # Vykreslime obrazek pozadi pres celou herni plochu (to nam "premaze" vse, co jsme vykreslili
    # v predchozim pruchodu cyklem)
    win.blit(obrazekPozadi, (0, 0))

    # Pokud je promenna "goblinUtoci" nastavena True (Pravda), tak budeme animovat utok
    if (goblinUtoci):
        if (cisloFramuUtoku < len(poleSnimkuUtoku)):
            if (aktualniCas - posledniPrekresleni > casMeziFramy):
                win.blit(poleSnimkuUtoku[cisloFramuUtoku], (150, 0))
                cisloFramuUtoku = cisloFramuUtoku + 1
                posledniPrekresleni = aktualniCas
            else:
                win.blit(poleSnimkuUtoku[cisloFramuUtoku], (150, 0))
        else:
            cisloFramuUtoku = 0
            goblinUtoci = False
            win.blit(poleSnimkuCekani[cisloFramu], (150, 0))
    # Promenna "goblinUtoci" je neni True (Pravda), takze budeme animovat cekani (postavani)
    else:
        if (aktualniCas - posledniPrekresleni > casMeziFramy):
            cisloFramu = cisloFramu + 1
            posledniPrekresleni = aktualniCas

        if (cisloFramu >= len(poleSnimkuCekani)):
            cisloFramu = 0

        win.blit(poleSnimkuCekani[cisloFramu], (150, 0))

    # Zavolame funkci "update", ktera vykresli vsechny zmeny na obrazovku
    pygame.display.update()

#### Tady konci hlavni herni cyklus ###

# Ukonceni pygame
pygame.quit()