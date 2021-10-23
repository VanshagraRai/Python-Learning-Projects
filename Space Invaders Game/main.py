import random

import pygame

# Initializing the pygame
pygame.init()

# Creating the screen ( Width , Height)
screen = pygame.display.set_mode((800, 600))

# Setting the Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("space-ship.png")
pygame.display.set_icon(icon)

# Setting Up the Player
playerImg = pygame.image.load("spaceship.png")
playerx = 370
playery = 500
playerx_update = 0


# Setting up the enemy
enemyImg = pygame.image.load("alien.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 450)
enemyX_update = 1
# enemyY_update = 0


# Player function
def player(x, y):
    screen.blit(playerImg, (x, y))


# Enemy function
def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Game Loop
running = True
while running:
    # Screen Background Color
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_update = -0.3
            if event.key == pygame.K_RIGHT:
                playerx_update = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerx_update = 0
            if event.key == pygame.K_RIGHT:
                playerx_update = 0

    # Preventing Player from going outside
    if playerx < 0:
        playerx = 0
    if playerx > 735:
        playerx = 735

    # Moving the Enemy
    enemyX += enemyX_update
    if enemyX > 735:
        enemyX = 735
        enemyX_update = -1
        enemyY += 10
    if enemyX < 0:
        enemyX = 0
        enemyX_update = 1
        enemyY += 10

    # Crashing of both the parties
    if playerx >= enemyX and playery <= enemyY:
        enemyX = 360
        enemyX_update = 0
        enemyY = 50

    playerx += playerx_update
    player(playerx, playery)


    enemy(enemyX, enemyY)
    pygame.display.update()
