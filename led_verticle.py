# Listing_16-17.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# move a beach ball image in a pygame window with wrapping

import pygame, sys, feedparser, twitter, wordwrap
c = 0
counter = 0
tweets = twitter.get_tweets()
pygame.init()
pygame.mouse.set_visible(0)
screen = pygame.display.set_mode([0,0] ,pygame.FULLSCREEN)
screen.fill([0, 0, 0])
font = pygame.font.SysFont('astronaut',100)
fontSize = font.size(tweets[c])
lines = wordwrap.wrapline(tweets[c],font, screen.get_width())
x = 0
y = screen.get_height()
y_speed = -5

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        sys.exit()

    pygame.time.delay(30)
    pygame.draw.rect(screen, [0,0,0], [x, y, fontSize[0], fontSize[1]], 0)
    y = y + y_speed
    if y < -int(fontSize[1] * len(lines)):
        c += 1
        font = pygame.font.SysFont('astronaut',100)
        lines = wordwrap.wrapline(tweets[c],font, screen.get_width())
        y = screen.get_height() + 100
        for i in range(len(lines)):
            text = font.render(lines[i] , False, (0,0,255), (0,0,0))
            screen.blit(text,[x,y - (-100 * i)])
            pygame.display.update()
        if c == 4:
            c = -1
            tweets = twitter.get_tweets()
        else:
            pass
    else:
        for i in range(len(lines)):
            text = font.render(lines[i] , False, (0,0,255), (0,0,0))
            screen.blit(text,[x,y - (-100 * i)])
            pygame.display.update()
