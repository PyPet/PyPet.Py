import pygame
import os
import sys

def game():
    fps = 10
    pygame.init()
    size = 432, 288
    win = pygame.display.set_mode(size)
    pygame.display.set_caption("PyPet.py")
    WHITE = 255, 255, 255
    BG_LOOP_IMG = pygame.image.load(os.path.join("assets", "bg-loop.png"))
    bg = pygame.transform.scale(BG_LOOP_IMG, size)


    width, height = size
    i = 0
    i2=True
    run = True
    clock = pygame.time.Clock()
    # light shade of the button
    color_light = (231, 76, 60)
    color_white = (236, 240, 241)
    # dark shade of the button
    color_dark = (192, 57, 43)
    pet_IMG = pygame.image.load(os.path.join("assets", "pet.png"))
    pet3 = pygame.transform.scale(pet_IMG, (110,100))
    pet2=pygame.transform.flip(pet3, True, False)
    while run:
        clock.tick(fps)
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
            win.blit(pet2, (size[0]/2, 175))
        else:
            i2=True
            win.blit(pet2, (size[0]/2, 170))
        smallfont = pygame.font.Font(os.path.join("assets", "font.ttf"),25)
        text = smallfont.render('Salir' , True , color_white)
        mouse = pygame.mouse.get_pos()
        if width/10 <= mouse[0] <= width/10+140 and height/10 <= mouse[1] <= height/10+40:
            pygame.draw.rect(win,color_light,[width/10,height/10,140,40])
          
        else:
            pygame.draw.rect(win,color_dark,[width/10,height/10,140,40])
        win.blit(text , (width/10+20,height/10+5))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key ==  pygame.K_F10:
                run=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width/10 <= mouse[0] <= width/10+140 and height/10 <= mouse[1] <= height/10+40:
                    pygame.quit()

if __name__ == '__main__':
    try: 
        game()
    except Exception as e:
        print("""-- Ha ocurrido el siguiente error --
-- Puedes ignorar el error, a vezes pasa al cerrar --""")
        print(e)