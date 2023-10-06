import pygame as pg

pg.init()

screen_width = 800
screen_height = 600

display = pg.display.set_mode((screen_width, screen_height))
display.fill('pink', (0, 0, screen_width, screen_height))

sysfont = pg.font.SysFont('arial', 40)
text_img = sysfont.render('Ye min htwe', True, 'red')


w = text_img.get_width()
h = text_img.get_height()
x = screen_width - w
y = screen_height/2 - h


running = True
while running:
    pg.display.update()
    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN and event.key == pg.K_q:
            running = False
        if event.type == pg.KEYUP and event.key == pg.K_y:
            print('Press y')
            display.blit(text_img, (x, y))

        if event.type == pg.KEYUP and event.key == pg.K_c:
            print('Press C')


pg.quit()

