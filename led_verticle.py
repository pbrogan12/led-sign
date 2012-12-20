# Listing_16-17.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# move a beach ball image in a pygame window with wrapping

import pygame, sys, feedparser, twitter, wordwrap, nfl
c = 0
color = (0,0,255)
tweets = twitter.get_tweets() + nfl.get_scores()
tweets.insert(0,"Welcome to the Brogan family thanksgiving.  Tweet with the hashtag #btd1122 to have your tweets displayed")
pygame.init()
pygame.mouse.set_visible(0)
screen = pygame.display.set_mode([0,0] ,pygame.FULLSCREEN)
screen.fill([0, 0, 0])
font = pygame.font.SysFont('clubland',100)
fontSize = font.size(tweets[c])
lines = wordwrap.wrapline(tweets[c],font, screen.get_width())
x = 0
y = screen.get_height()
y_speed = -5

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.key == pygame.K_g:
            color = (0,255,0)
        if event.key == pygame.K_r:
            color = (255,0,0)
        if event.key == pygame.K_b:
            color = (0,0,255)
        if event.key == pygame.K_w:
            color = (255,255,255)

    pygame.time.delay(30)
    y = y + y_speed
    if y < -int(fontSize[1] * len(lines)):
        c += 1
        font = pygame.font.SysFont('clubland',100)
        lines = wordwrap.wrapline(tweets[c],font, screen.get_width())
        y = screen.get_height() + 100
        for i in range(len(lines)):
            t = str(lines[i].encode('ascii','replace'))
            text = font.render(t, False, color, (0,0,0))
            screen.blit(text,[x,y - (-100 * i)])
        if c == len(tweets) - 1:
            c = -1
            tweets = twitter.get_tweets() + nfl.get_scores()
            tweets.insert(0,"Welcome to the Brogan family thanksgiving.  Tweet with the hashtag #btd1122 to have your tweets displayed")
        else:
            pass
    else:
        for i in range(len(lines)):
            text = font.render(lines[i] , False, color , (0,0,0))
            screen.blit(text,[x,y - (-100 * i)])
    pygame.display.update()
