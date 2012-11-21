# Listing_16-17.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# move a beach ball image in a pygame window with wrapping

import pygame, sys, feedparser, twitter
c = 0
tweets = twitter.get_tweets()
pygame.init()
pygame.mouse.set_visible(0)
screen = pygame.display.set_mode([0,0] ,pygame.FULLSCREEN)
screen.fill([0, 0, 0])
font = pygame.font.SysFont('astronaut',250)
text = font.render(tweets[c] , False, (0,0,255), (0,0,0))
fontSize = font.size(tweets[c])
x = screen.get_width()
y = screen.get_height() / 2
x_speed = -10

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        sys.exit()

    pygame.time.delay(30)
    pygame.draw.rect(screen, [0,0,0], [x, y, fontSize[0], fontSize[1]], 0)
    x = x + x_speed
    if x < -int(fontSize[0]):
        c += 1
        font = pygame.font.SysFont('astronaut',250)
        text = font.render(tweets[c], False, (0,0,255), (0,0,0) )
        fontSize = font.size(tweets[c])
        x = screen.get_width() + 100
        screen.blit(text, [x, y])
        pygame.display.update()
        if c == 4:
            c = 0
            twitter.get_tweets()
        else:
            pass
    else:
        screen.blit(text, [x, y])
        pygame.display.update()
