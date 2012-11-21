# Listing_16-17.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# move a beach ball image in a pygame window with wrapping

import pygame, sys, feedparser
print "BAT"
d = feedparser.parse('http://www.sportsnetwork.com/aspdata/clients/sportsnetwork/NFLrssscores.aspx')
c = 0
t = 0
msg = ""
msg1 = ""
for i in d.entries:
    a = i.title
    if c / 2 == 1:
        msg = msg + ' ' + a
        c += 1
    else:
        msg1 = msg1 + ' ' + a
        c += 1
pygame.init()
pygame.mouse.set_visible(0)
screen = pygame.display.set_mode([0,0] ,pygame.FULLSCREEN)
screen.fill([0, 0, 0])
font = pygame.font.SysFont('astronautiii',75)
text = font.render(msg + msg1, False, (255,0,0))
fontSize = font.size(msg + msg1)
x = screen.get_width() + 40
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
    if x < -int(fontSize[0]) + -60:
        t += 1
        if t >= 2:
            msg = "FOOOOOOOOOOOOOOOOOOBAT"
            msg1 = "THISISTHEBOMB"
            font = pygame.font.SysFont('astronaut',100)
            text = font.render(msg + msg1, False, (255,0,0))
            print text, msg, msg1
            x = 1080
            screen.blit(text, [x, y])
            pygame.display.update()
        else:
            x = 1080
            screen.blit(text, [x, y])
            pygame.display.update()
    else:
        screen.blit(text, [x, y])
        pygame.display.update()
