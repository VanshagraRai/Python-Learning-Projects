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

# Setting the background Image
bg = pygame.image.load("pexels-hristo-fidanov-1252890.jpg")

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

# Setting up the Bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 385
bulletY = 500
# bulletX_update = 1
bulletY_update = -1
bullet_state = "Ready"  # To check the state of bullet whether it is ready or firing


# Player function
def player(x, y):
    screen.blit(playerImg, (x, y))


# Enemy function
def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Bullet Function
def bullet(x, y):
    global bullet_state
    bullet_state = "Firing"
    screen.blit(bulletImg, (x + 17, y + 2))


# Game Loop
running = True
while running:
    # Screen Background Color
    # screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_update = -0.3
            if event.key == pygame.K_RIGHT:
                playerx_update = 0.3
            if event.key == pygame.K_SPACE:
                bullet(bulletX, bulletY)
                # bullet_state = "Firing"
                # if bullet_state == "Firing":
                #

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerx_update = 0
            if event.key == pygame.K_RIGHT:
                playerx_update = 0
            # if event.key == pygame.K_SPACE:
            #     bullet_state = "Ready"


    # Preventing Player from going outside
    if playerx < 0:
        playerx = 0
    if playerx > 735:
        playerx = 735

    playerx += playerx_update

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



    # Moving the bullet
    if bullet_state == "Firing":
        bulletY += bulletY_update
    #
    #
    # if
    #
    #     bullet_state = "Ready"
    #
    #     bulletX = playerx
    # # bulletY = playery
    if bulletY == 0:
        bulletX = playerx
        bulletY = playery
        bulletY_update = 0
    bullet(bulletX, bulletY)
    player(playerx, playery)
    

    enemy(enemyX, enemyY)
    pygame.display.update()
