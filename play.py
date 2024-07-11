# this is the play button code
import pygame as game
import colours as c  

game.init()
# setting an update fuction
def update():
    game.display.update()

# creating gamewindow
game.display.set_caption("TIC-TAC-TAO")
screenwidth = 500
screenheight = 500
gamewindow = game.display.set_mode((screenwidth, screenheight))
clock=game.time.Clock()

# background image load
play_image=game.image.load('front.png')
play_image=game.transform.scale(play_image,(screenheight,screenwidth)).convert_alpha()

# loading a music
game.mixer.init()
game.mixer.music.load("beep.mp3")

game.mixer.music.load("start.mp3")

# gamingloop
def playgame():
    exit_game=False
    game.mixer.music.play()
    while not exit_game:
        mx,my=game.mouse.get_pos()
        gamewindow.fill(c.white)
        gamewindow.blit(play_image,(0,0))
        
        for event in game.event.get():
            if (event.type==game.QUIT):
                exit_game=True
            if (118 < mx < 362) and (188 < my <273):
                if(event.type==game.MOUSEBUTTONDOWN):
                    if (game.mouse.get_pressed()[0]):
                        import test
            if (118 < mx < 362) and (327 < my <416):
                if(event.type==game.MOUSEBUTTONDOWN):
                    if (game.mouse.get_pressed()[0]):
                        import multiplayer
            # print(event)
            update()
            clock.tick(60)
playgame()