import pygame
import os
import sys

def game(fs = 0):
    fps = 10
    pygame.init()
    size = 432, 288
    win = pygame.display.set_mode(size, fs, 32)
    pygame.display.set_caption("PyPet.py")
    WHITE = 255, 255, 255
    BG_LOOP_IMG = pygame.image.load(os.path.join("assets", "bg-loop.png"))
    bg = pygame.transform.scale(BG_LOOP_IMG, size)


    width = 432
    i = 0
    i2=True
    run = True
    clock = pygame.time.Clock()

    pet_IMG = pygame.image.load(os.path.join("assets", "pet.png"))
    pet3 = pygame.transform.scale(pet_IMG, (110,100))
    pet2=pygame.transform.flip(pet3, True, False)
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key ==  pygame.K_F10:
                run=False
        win.fill((0, 0, 0))
        # Create looping background
        win.blit(bg, (i, 0))
        win.blit(bg, (width+i, 0))
        if i == -width:
            win.blit(bg, (width+i, 0))
            i = 0
        i -= 4
        if i2 == True:
            i2=False
            pet = win.blit(pet2, (size[0]/2, 175))
        else:
            i2=True
            pet = win.blit(pet2, (size[0]/2, 170))
        pygame.display.update()

if __name__ == '__main__':
    try:
        print("ARGS: " + sys.argv[1])
        if sys.argv[1] == "--pypetDIY": game(-2147483648)
    except:
        game(0)