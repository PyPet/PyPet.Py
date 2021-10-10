import pygame
import os
import yaml
import sentry_sdk
import modules

sentry_sdk.init(
    "https://4539e0ffd7a94bbb8041ac9fefdbd1fe@o555373.ingest.sentry.io/5972323",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
)


# Cuarquier traduccion en la carpeta translations
# Any translations in the translations folder
lang = "es"

with open("./translations/" + lang.lower() + ".yaml", "r") as s:
    config = yaml.safe_load(s)
    s.close()


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
    PET_IMG = pygame.transform.flip(pygame.transform.scale(
        pygame.image.load(os.path.join("assets", "pet.png")), (110, 100)), True, False)
    BG_LOOP_IMG = pygame.transform.scale(pygame.image.load(
        os.path.join("assets", "bg-loop.png")), WIN_SIZE)

    # Especificamos las variables extra
    # We specify the extra variables
    BG_POS = 0
    PET_EXTRA_5px = True
    APP_RUN = True

    # Especificamos los colores
    # We specify the colors
    COLOR_BTN_LIGHT = (231, 76, 60)
    COLOR_BTN_DARK = (192, 57, 43)
    COLOR_FONT_WHITE = (236, 240, 241)
    COLOR_BLACK = (0, 0, 0)

    # Especificamos la fuente
    # We specify the source
    FONT_SMALL = pygame.font.Font(os.path.join("assets", "font.ttf"), 25)

    # Creamos el boton "Salir"
    # We make the "Exit" Button
    button_exit = modules.Button()
    button_exit.extras = (WIN_SIZE, (10,10), pygame, WIN, COLOR_BTN_DARK, COLOR_BTN_LIGHT, FONT_SMALL, COLOR_FONT_WHITE, config["exitBtn"])

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
            PET_EXTRA_5px = False
            WIN.blit(PET_IMG, (WIN_SIZE[0]/2, 175))
        else:
            PET_EXTRA_5px = True
            WIN.blit(PET_IMG, (WIN_SIZE[0]/2, 170))

        # Mostramos el boton
        # We display the button
        button_exit.display()

        # Actualizamos la ventana
        # We update the window
        pygame.display.update()

        # Detectamos los eventos
        # We detect events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                APP_RUN = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_F10:
                APP_RUN = False
            if button_exit.isClicked(event):
                pygame.quit()


if __name__ == '__main__':
    try:
        game()
    except Exception as e:
        print(config["error"])
        print(e)

