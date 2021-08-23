import pygame
import os
fps = 30
pygame.init()
size = 480, 320
pygame.display.set_caption("PyPet.py")
WHITE = 255, 255, 255
BG_LOOP_IMG = pygame.image.load(os.path.join("assets", "bg-loop.png"))
bg = pygame.transform.scale(BG_LOOP_IMG, size)
win = pygame.display.set_mode(size)


width = -480
i = 0
i2=True
run = True
clock = pygame.time.Clock()

pet_IMG = pygame.image.load(os.path.join("assets", "pet.png"))
pet2 = pygame.transform.scale(pet_IMG, (110,100))
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((0, 0, 0))
    # Create looping background
    win.blit(bg, (i, 0))
    win.blit(bg, (width+i, 0))
    if i == -width:
        win.blit(bg, (width+i, 0))
        i = 0
    i += 5
    if i2 == True:
        i2=False
        pet = win.blit(pet2, (200, 215))
        clock.tick(10)
    else:
        i2=True
        pet = win.blit(pet2, (200, 210))
        clock.tick(10)
    pygame.display.update()
