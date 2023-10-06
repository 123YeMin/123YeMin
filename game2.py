import pygame as pg

pg.init()

screen_width = 800
screen_height = 600

display = pg.display.set_mode((screen_width, screen_height))
display.fill('pink', (0, 0, screen_width, screen_height))
#pg.display.set_caption('Космическое вторжение')
#icon_img = pg.image.load('resources/img/ufo.png')
#pg.display.set_icon(icon_img)

background_img = pg.image.load('resources/img/background.png')
display.blit(background_img, (0, 0))

# шрифт для букв
sysfont = pg.font.SysFont('arial', 40)
text_img = sysfont.render('Score: 123', True, 'red')

#font = pg.font.Font('resources/font/04B_19__.TTF', 48)
#game_over_img = font.render('Game Over', True, 'white')
w = game_over_img.get_width()
h = game_over_img.get_height()
x = screen_width/2 - w/2
y = screen_height/2 - h/2
display.blit(game_over_img, (x, y))

player_img = pg.imgame.load('resources/img/player.png')
player_width = player_img.get_width()
player_height = player_img.get.height()
player_x = screen_width/2 - player_width/2
player_y = screen_height - player_height
player_velocity = 1
Player_dx= 0

bullet_img = pg.imgame.load('resources/img/player.png')
bullet_width = bullet_img.get_width()
bullet_height = bullet_img.get.height()
bullet_x = 0
bullet_y = 0
bullet_dy = -2



y = screen_height - bullet_height
player_velocity = 1
Player_dy = -2

running = True
while running:
    # рисовать
    #display.fill('blue', (20, 50, 100, 250))

    player_x = player_x + player_dx
    if player_x < 0:
        player_x = 0
    bullet_y = bullert_y + bullet_dy
    if player_y < 0:
        bullet_visible = flase
        print(f"{bullet_visible=}")

    display.blit(background_img, (0, 0))
    display_blit(player_img,(player_x,player_y))
    display_blit(bullet_img,(player_x,player_y))
    pg.display.update()


    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN and event.key == pg.K_q:
            running = False

        if event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
            Player_dx=player_velocity
        if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
            Player_dx=player_velocity

        if event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
            Player_dx= - 0

        if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
            Player_dx=player_velocity



pg.quit()