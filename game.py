import random
import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((480, 480))

# Background
background = pygame.image.load('floor.png')

# Sound
mixer.music.load("soviet_march.wav")
mixer.music.play(-1)

pygame.display.set_caption("Perspectives") #Game title
icon = pygame.image.load('hero.png') #Imgae icon
pygame.display.set_icon(icon) 

playerImg = pygame.image.load('hero.png') #Load in the image of the player
playerX = 400 #Player starting coordinates
playerY = 400
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies): #Load number of enemies in a for loop
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736)) #Spawn enemy at random x coordinate
    enemyY.append(random.randint(50, 150)) #Spawn enemy at random y coordinate
    enemyX_change.append(4) 
    enemyY_change.append(40)

wall = pygame.image.load('wall2.png') #Load image of wall behind which hero hides

def player(x, y): #define function to place hero in certain coordinates
    screen.blit(playerImg, (x, y)) #scree.blit places image on the screen


def enemy(x, y, i): #define function to place enemy in certain coordinates
    screen.blit(enemyImg[i], (x, y))

# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0)) #Fill the screen with black
    # Background Image
    screen.blit(background, (0, 0)) #add background layer
    screen.blit(wall, (360, 370)) #add wall
    for event in pygame.event.get(): #if user presses x then quit
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1 #Change the value of playerX_change
            if event.key == pygame.K_RIGHT:
                playerX_change = 1 #Change the value of playerX_change
            if event.key == pygame.K_UP:
                playerY_change = -1 #Change the value of playerY_change
            if event.key == pygame.K_DOWN:
                playerY_change = 1 #Change the value of playerY_change

        if event.type == pygame.KEYUP: #If user leaves the key, then stop moving 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0
               
    playerX += playerX_change #Add the value of playerX_change to players x coordinate 
    playerY += playerY_change #Add the value of playerY_change to players y coordinate
   
    if playerX <= 0: #If player goes outside the boundary teleport them back in
        playerX = 0
    elif playerX >= 449:
        playerX = 449
    if playerY <= 0:
        playerY = 0
    elif playerY >= 449:
        playerY = 449
       
    # Enemy Movement
    for i in range(num_of_enemies):

        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]

        enemy(enemyX[i], enemyY[i], i)
     
    player(playerX, playerY) #place player in the desired position
    pygame.display.update() #update the screen
