import pygame as pg

pg.init()

screen_width = 800
screen_height = 600

display = pg.display.set_mode((screen_width, screen_height))
display.fill('light blue', (0, 0, screen_width, screen_height))


background_img = pg.image.load('resources/img/background.png')
display.blit(background_img, (0, 0))

# шрифт для букв
sysfont  = pg.font.SysFont('arial', 40)
text_img = sysfont.render('Ye Min Htwe ', True, 'red')

w = text_img.get_width()
h = text_img.get_height()
x = screen_width/2 - w/2
y = screen_height/2 -(h*2)


player_img = pg.image.load('resources/img/player.png')
player_width = player_img.get_width()
player_height = player_img.get_height()
player_x = screen_width/2 - player_width/2
player_y = screen_height - player_height

player_dx= 0
player_velocity = 1

bullet_img = pg.image.load('resources/img/bullet.png')
bullet_width = bullet_img.get_width()
bullet_height = bullet_img.get_height()
bullet_x = player_x
bullet_y = player_y - bullet_height
bullet_dy = -2
bullet_visible = False

def bullet_create():
    global bullet_y, bullet_x, bullet_visible
    bullet_x = player_x
    bullet_y = player_y - bullet_height
    bullet_visible = True

def model_update():
    player_model()
    bullet_model()

def player_model():
    global player_x
    player_x = player_x + player_dx
    if player_x < 0:
        player_x = 0

    if player_x + player_width > screen_width:
        player_x = screen_height - screen_width

def bullet_model():
    global bullet_visible, bullet_y
    if bullet_visible:
        bullet_y = bullet_y + bullet_dy
        if bullet_y < 0:
            bullet_visible = False
            print(f"{bullet_visible}")

def redraw():
    display.blit(background_img, (0, 0))
    display.blit(player_img, (player_x, player_y))
    if bullet_visible:
        display.blit(bullet_img, (bullet_x, bullet_y))

    pg.display.update()


def event_process():
    global player_dx
    running = True
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN and event.key == pg.K_q:
            running = False

        if event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
            player_dx = - player_velocity
        if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
            player_dx = player_velocity

        if event.type == pg.KEYUP and event.key == pg.K_LEFT:
            player_dx = 0

        if event.type == pg.KEYUP and event.key == pg.K_RIGHT:
            player_dx = 0

    # Fire!
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            if not bullet_visible:
                bullet_create()
                print('Fire!')

    return running
running  = True
while running:
    model_update()
    redraw()
    running = event_process()





pg.quit()