import pygame
# Initializing the pygame
pygame.init()

#Creating the screen ( Width , Height)
screen = pygame.display.set_mode((800, 600))


# Setting the Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("space-ship.png")
pygame.display.set_icon(icon)


# Setting Up the Player
playerImg = pygame.image.load("spaceship.png")
playerx = 370
playery = 500

# Player function

def player():
    screen.blit(playerImg, (playerx, playery))


# Game Loop
running = True
while running:
    # Screen Background Color
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()