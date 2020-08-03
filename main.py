import pygame
# Starts the game
pygame.init()
screen = pygame.display.set_mode((800, 700))  # Screen is created Width and Height

# Title and icon
pygame.display.set_caption("Space Invaders")
icono = pygame.image.load('astronave.png')
pygame.display.set_icon(icono)

# This is to make sure the screen doesnt close (Game loop_
running = True;
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;

    # RGB - red, green, blue
    screen.fill((0, 100, 170))
    pygame.display.update() # this is necessary in every game

