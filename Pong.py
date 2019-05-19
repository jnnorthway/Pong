import pygame
import sys
import time
import random
from pygame.locals import *
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('arial', 40)

h = 700
WIDTH = 800
HEIGHT = 600
WHITE = (255,255,255)
GOLD = (255,215,0)
RED = (255, 0, 0)
BACKGROUND = (0,0,0)

#player
pL = 10
pW = 100
speed = 10

p1X = 0
p1Y = int(h-HEIGHT + HEIGHT/2)
p1Score = 0

p2X = WIDTH - pL
p2Y = int(h-HEIGHT + HEIGHT/2)
p2Score = 0

#gameSpeed = 0.01
gameSpeed = 0.005

#ball
bR = 10
bX = int(WIDTH/2)
bY = int(h-HEIGHT + HEIGHT/2)
bSpeed = 5
bYSpeed = 0

hits = 0

players = int(input("How many players? (1/2): "))


pygame.display.set_caption("Game!")
screen = pygame.display.set_mode((WIDTH, h))
pygame.key.set_repeat(1,speed)

game_over = False

def update():
    screen.fill(BACKGROUND)

    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, h-HEIGHT))
    pygame.draw.rect(screen, RED, (10, 10, h-HEIGHT-20, h-HEIGHT-20))
    pygame.draw.rect(screen, RED, (WIDTH - 10 - (h-HEIGHT-20), 10, h-HEIGHT-20, h-HEIGHT-20))
    textsurface = myfont.render(str(p1Score), False, BACKGROUND)
    screen.blit(textsurface,(40,25))
    textsurface = myfont.render(str(p2Score), False, BACKGROUND)
    screen.blit(textsurface,(WIDTH-55,25))

    pygame.draw.line(screen, WHITE, (WIDTH/2, h-HEIGHT), (WIDTH/2, h))

    pygame.draw.circle(screen, GOLD, (bX, bY), bR)
    pygame.draw.rect(screen, WHITE, (p1X, p1Y, pL, pW))
    pygame.draw.rect(screen, WHITE, (p2X, p2Y, pL, pW))
    pygame.display.update()

def printScore():
    print(str(p1Score) + " : " + str(p2Score))


start = time.time()

wait = True

while wait:
    update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            wait = False

while not game_over:

    time.sleep(gameSpeed)

    if hits >= 1:
        bSpeed += 1
        hits = 0

    update()
    if (bX >= WIDTH - bR - pL) or (bX <= bR + pL):
        if bY >= p1Y and bY <= p1Y + pW and bX <= WIDTH/2:
            bSpeed*=-1
            hits += 1
            if bY >= p1Y and bY <= p1Y + pW/3:
                if bYSpeed >= -1:
                    bYSpeed += -1
            elif bY >= p1Y + 2/3*pW and bY <= p1Y + pW:
                if bYSpeed <= 1:
                    bYSpeed += 1
        elif bY >= p2Y and bY <= p2Y + pW and bX >= WIDTH/2:
            bSpeed*=-1
            if bY >= p2Y and bY <= p2Y + pW/3:
                if bYSpeed >= -1:
                    bYSpeed += -1
            elif bY >= p2Y + 2/3*pW and bY <= p2Y + pW:
                if bYSpeed <= 1:
                    bYSpeed += 1
        elif (bX >= WIDTH + bR):
            p1Score += 1
            printScore()
            if p1Score >= 10:
                print("Player 1 wins!")
                game_over = True
            p1Y = int(h-HEIGHT + HEIGHT/2)
            p2Y = int(h-HEIGHT + HEIGHT/2)
            bX = int(WIDTH/2)
            bY = int(h-HEIGHT + HEIGHT/2)
            bSpeed = 5
            bYSpeed = 0
            update()
            time.sleep(1)

        elif (bX <= bR):
            p2Score += 1
            printScore()
            if p2Score >= 10:
                print("Player 2 wins!")
                game_over = True
            p1Y = int(h-HEIGHT + HEIGHT/2)
            p2Y = int(h-HEIGHT + HEIGHT/2)
            bX = int(WIDTH/2)
            bY = int(h-HEIGHT + HEIGHT/2)
            bSpeed = -5
            bYSpeed = 0
            update()
            time.sleep(1)


    bX += bSpeed
    bY += bYSpeed

    if bY + bR >= h-HEIGHT + HEIGHT or bY - bR <= h-HEIGHT:
        bYSpeed *= -1

    if players == 1:
        if bY < p2Y + 1/3*pW:
            p2Y -= 1
        elif bY > p2Y + 2/3*pW:
            p2Y += 1


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and p1Y >= h-HEIGHT:
                p1Y -= 10
            if event.key == pygame.K_DOWN and p1Y <= h-HEIGHT + HEIGHT - pW:
                p1Y += 10
            if event.key == pygame.K_LEFT and p1Y >= h-HEIGHT:
                p1Y -= 10
            if event.key == pygame.K_RIGHT and p1Y <= h-HEIGHT + HEIGHT - pW:
                p1Y += 10
            if players == 2:
                if event.key == pygame.K_w and p2Y >= h-HEIGHT:
                    p2Y -= 10
                if event.key == pygame.K_s and p2Y <= h-HEIGHT + HEIGHT - pW:
                    p2Y += 10


end = time.time()
