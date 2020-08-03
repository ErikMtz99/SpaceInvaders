import pygame

# Starts the game
pygame.init()
screen = pygame.display.set_mode((800, 600))  # Screen is created Width and Height

# Title and icon
pygame.display.set_caption("Space Invaders")
icono = pygame.image.load('astronave.png')
pygame.display.set_icon(icono)

# Player
playerImg = pygame.image.load('astronave64.png')
playerX = 350
playerY = 400


def player(x, y):
    screen.blit(playerImg, (x, y))


# This is to make sure the screen doesnt close (Game loop_
running = True
while running:

    # RGB - red, green, blue
    screen.fill((0, 100, 170))
    playerY -= 0.1
    playerX += 0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player(playerX, playerY)
    pygame.display.update()  # this is necessary in every game
