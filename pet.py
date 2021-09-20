import pygame
import os
import sys

def game():
    # Cambia esto por tu ratio de FPS
    # Change this with your FPS rate
    FPS = 10

    # Inicializamos pygame
    # We initialize pygame
    pygame.init()

    # Especificamos el tamaño de la ventana
    # We specify the SIZE of the window
    WIN_SIZE = 432, 288

    # Iniciamos la ventana
    # We start the window
    WIN = pygame.display.set_mode(WIN_SIZE)
    pygame.display.set_caption("PyPet.py")

    # Especificamos los sprites
    # We specify the sprites
    PET_IMG = pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join("assets", "pet.png")), (110,100)), True, False)
    BG_LOOP_IMG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "bg-loop.png")), WIN_SIZE)

    # Especificamos las variables extra
    # We specify the extra variables
    BG_POS = 0
    PET_EXTRA_5px=True
    APP_RUN = True

    # Especificamos los colores
    # We specify the colors
    COLOR_BTN_LIGHT = (231, 76, 60)
    COLOR_BTN_DARK = (192, 57, 43)
    COLOR_FONT_WHITE = (236, 240, 241)
    COLOR_BLACK = (0, 0, 0)

    # Especificamos la fuente
    # We specify the source
    FONT_SMALL = pygame.font.Font(os.path.join("assets", "font.ttf"),25)

    # Iniciamos el bucle del juego
    # We start the game loop
    while APP_RUN:
        # Hacemos un Tick
        # We make a tick
        pygame.time.Clock().tick(FPS)

        # Creamos el fondo
        # We create the background
        WIN.blit(BG_LOOP_IMG, (BG_POS, 0))
        WIN.blit(BG_LOOP_IMG, (WIN_SIZE[0]+BG_POS, 0))
        if BG_POS == -WIN_SIZE[0]:
            WIN.blit(BG_LOOP_IMG, (WIN_SIZE[0]+BG_POS, 0))
            BG_POS = 0
        BG_POS -= 4

        # Creamos el sprite
        # We create the sprite
        if PET_EXTRA_5px == True:
            PET_EXTRA_5px=False
            WIN.blit(PET_IMG, (WIN_SIZE[0]/2, 175))
        else:
            PET_EXTRA_5px=True
            WIN.blit(PET_IMG, (WIN_SIZE[0]/2, 170))

        # Hacemos el boton
        # We make the button
        if WIN_SIZE[0]/10 <= pygame.mouse.get_pos()[0] <= WIN_SIZE[0]/10+140 and WIN_SIZE[1]/10 <= pygame.mouse.get_pos()[1] <= WIN_SIZE[1]/10+40:
            pygame.draw.rect(WIN,COLOR_BTN_LIGHT,[WIN_SIZE[0]/10,WIN_SIZE[1]/10,140,40])
        else:
            pygame.draw.rect(WIN,COLOR_BTN_DARK,[WIN_SIZE[0]/10,WIN_SIZE[1]/10,140,40])
        WIN.blit(FONT_SMALL.render('Salir' , True , COLOR_FONT_WHITE) , (WIN_SIZE[0]/10+20,WIN_SIZE[1]/10+5))

        # Actualizamos la ventana
        # We update the window
        pygame.display.update()

        # Detectamos los eventos
        # We detect events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                APP_RUN = False
            if event.type == pygame.KEYDOWN and event.key ==  pygame.K_F10:
                APP_RUN=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIN_SIZE[0]/10 <= pygame.mouse.get_pos()[0] <= WIN_SIZE[0]/10+140 and WIN_SIZE[1]/10 <= pygame.mouse.get_pos()[1] <= WIN_SIZE[1]/10+40:
                    pygame.quit()

if __name__ == '__main__':
    try: 
        game()
    except Exception as e:
        print("""--          Ha ocurrido el siguiente error          --
-- Puedes ignorar el error, a vezes pasa al cerrar. --""")
        print(e)