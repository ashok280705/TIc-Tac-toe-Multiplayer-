import pygame as game
import colours as c
import cross as cc
import circle as o
game.init()

# setting a game caption
game.display.set_caption('NEW TIC-TAC-TOE GAME')

# creating a game window
screenwidth = 500
screenheight = 500
gamewindow = game.display.set_mode((screenwidth, screenheight))
clock = game.time.Clock()

# creating a font
font=game.font.SysFont(None,57)

# loading a music
game.mixer.init()
game.mixer.music.load("beep.mp3")


# loading background image
bgimg = game.image.load("tic-tac back.png")
bgimg = game.transform.scale(bgimg, (screenheight, screenwidth)).convert_alpha()

oimg=game.image.load('o.png')
oimg=game.transform.scale(oimg,(115,115)).convert_alpha()

ximg=game.image.load('x.png')
ximg=game.transform.scale(ximg,(115,115)).convert_alpha()

cimg=game.image.load('choice.png')
cimg=game.transform.scale(cimg,(screenheight,screenwidth)).convert_alpha()

dimg=game.image.load('DRAW.png')
dimg=game.transform.scale(dimg,(screenheight,screenwidth)).convert_alpha()

# winning combinations
winning_combinations=[
    [(58,56),(185,56),(310,56)],
    [(58,188),(185,188),(310,188)],
    [(58,320),(190,320),(320,320)],                 #horizonatal
    [(58,56),(58,188),(58,320)],
    [(185,56),(185,188),(190,320)],
    [(310,56),(310,188),(320,320)],                 #vertical
    [(58,56),(185,188),(320,320)],
    [(310,56),(185,188),(58,320)]
]
circle_combinations=[]
cross_combinations=[]

# draw combinations
updated_combinations=[]

# making combination none
def nonecomb():
    global circle_combinations
    global cross_combinations
    cross_combinations.clear()
    circle_combinations.clear()
    cc.cross_position1 = None
    cc.cross_position2=None
    cc.cross_position3=None
    cc.cross_position4=None
    cc.cross_position5=None
    cc.cross_position6=None
    cc.cross_position7=None
    cc.cross_position8=None
    cc.cross_position9=None
    
    o.circle_position1=None
    o.circle_position2=None
    o.circle_position3=None
    o.circle_position4=None
    o.circle_position5=None
    o.circle_position6=None
    o.circle_position7=None
    o.circle_position8=None
    o.circle_position9=None
# gameover loop
def game_over():
    fps=120
    game_exit=False
    while not game_exit:
        global updated_combinations
        updated_combinations.clear()
        gamewindow.fill(c.white)
        gamewindow.blit(cimg,(0,0))
        mx, my = game.mouse.get_pos()
        for event in game.event.get():
            if event.type == game.QUIT:
                with open('score1.txt','w') as f:
                    f.write("00")
                with open('score2.txt','w') as r:
                    r.write("00")
                game_exit = True
            if ((124 < mx < 380) and (103 < my <198)):
                if event.type == game.MOUSEBUTTONDOWN:
                        if game.mouse.get_pressed()[0]:
                            # print("hi")
                            gameloop()
            
            elif ((124 < mx < 380) and (287 < my <374)):
                if event.type == game.MOUSEBUTTONDOWN:
                        if game.mouse.get_pressed()[0]:
                            with open('score1.txt','w') as f:
                                f.write('00')
                            with open('score2.txt','w') as f:
                                f.write('00')
                            game_exit=True
        update()
        clock.tick(fps)
    game.quit()
    quit()
# setting a update function
def update():
    game.display.update()

# checking winner
def check_winner(symbol_positions):
    for combination in winning_combinations:
        if all(pos in symbol_positions for pos in combination):
            return True
    return False

# checking draw
def draw():
    global updated_combinations
    game_quit= False
    fps=60
    while not game_quit:
        gamewindow.fill(c.white)
        gamewindow.blit(dimg,(0,0))
        for event in game.event.get():
            if event.type == game.QUIT:
                game_quit==True
            if event.type == game.KEYDOWN:
                if event.key== game.K_SPACE:
                    game_over()
        update()
        clock.tick(fps)
    game.quit()
    quit()
                
# text fuction
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x,y])
    
# gaming loop
def gameloop():
    global draw_combinations
    global updated_combinations
    # setting exit variables
    game_quit = False
    fps = 60
    score=0
    while not game_quit:
        f=open('score1.txt','r') 
        read=f.read()
        f.close
        
        f=open('score2.txt','r') 
        read1=f.read()
        f.close 
         
        mx, my = game.mouse.get_pos()
        gamewindow.fill(c.white)
        gamewindow.blit(bgimg, (0, 0))
        text_screen(str(read),c.black,116,5)
        text_screen(str(read1),c.black,422,5)
        for event in game.event.get():
            # print(updated_combinations)
            if event.type == game.QUIT:
                with open('score1.txt','w') as f:
                    f.write("00")
                with open('score2.txt','w') as r:
                    r.write("00")
                game_quit = True
            # when player chooses o
            if (55 < mx < 180) and (54 < my < 180):
                if event.type == game.MOUSEBUTTONDOWN:
                    if game.mouse.get_pressed()[0]:             #1
                        # Update circle position
                        game.mixer.music.play()
                        o.circle_position1 = (58,56)
                        circle_combinations.append(o.circle_position1)
                        updated_combinations.append((58,56))
                        if len(updated_combinations)==9:
                            nonecomb()
                            game_over()
                            game_quit=True
            # print(event)
            if((180 < mx <310) and (55 < my < 180)):
                if event.type==game.MOUSEBUTTONDOWN:
                    if game.mouse.get_pressed()[0]:             #2
                        # update the cross position
                        game.mixer.music.play()
                        o.circle_position2=(185,56)
                        circle_combinations.append(o.circle_position2)
                        updated_combinations.append((185,56))
                        if len(updated_combinations)==9:
                            nonecomb()
                            game_over()
                            game_quit=True
            if((310 < mx < 435) and (55 < my < 180)):
                if event.type==game.MOUSEBUTTONDOWN:
                    if game.mouse.get_pressed()[0]: 
                        game.mixer.music.play()#3
                        o.circle_position3=(310,56)     
                        circle_combinations.append(o.circle_position3)  
                        updated_combinations.append((310,56))
                        if len(updated_combinations)==9:
                            nonecomb()
                            game_over()
                            game_quit=True    
            if((55 < mx < 180) and (180 < my < 310)):
                if event.type==game.MOUSEBUTTONDOWN:
                    if game.mouse.get_pressed()[0]:             #4
                        game.mixer.music.play()
                        o.circle_position4=(58,188) 
                        circle_combinations.append(o.circle_position4)
                        updated_combinations.append((58,188) )
                        if len(updated_combinations)==9:
                            nonecomb()
                            game_over()
                            game_quit=True
            if((180 < mx <310) and (180 < my < 310)):
                if event.type==game.MOUSEBUTTONDOWN:
                    if game.mouse.get_pressed()[0]:
                        game.mixer.music.play()                 #5
                        o.circle_position5=(185,188)  
                        circle_combinations.append(o.circle_position5)
                        updated_combinations.append((185,188))
                        if len(updated_combinations)==9:
                            nonecomb()
                            game_over()
                            game_quit=True
            if((310 < mx < 435) and (180 < my < 310)):
                if event.type==game.MOUSEBUTTONDOWN:
                    if game.mouse.get_pressed()[0]:             #6
                        game.mixer.music.play()
                        o.circle_position6=(310,188) 
                        circle_combinations.append(o.circle_position6)
                        updated_combinations.append((310,188))
                        if len(updated_combinations)==9:
                            nonecomb()
                            game_over()
                            game_quit=True
            if((55 < mx < 180) and (310 < my < 435)):
                if event.type==game.MOUSEBUTTONDOWN:
                    if game.mouse.get_pressed()[0]:             #7
                        game.mixer.music.play()
                        o.circle_position7=(58,320)
                        circle_combinations.append(o.circle_position7)
                        updated_combinations.append((58,320))
                        if len(updated_combinations)==9:
                            nonecomb()
                            game_over()
                            game_quit=True
            if((180 < mx <310) and (310 < my < 435)):
                if event.type==game.MOUSEBUTTONDOWN:
                    if game.mouse.get_pressed()[0]:             #8
                        game.mixer.music.play()
                        o.circle_position8=(190,320)
                        circle_combinations.append(o.circle_position8)
                        updated_combinations.append((190,320))
                        if len(updated_combinations)==9:
                            nonecomb()
                            game_over()
                            game_quit=True
            if((310 < mx < 435) and (310 < my < 435)):
                if event.type==game.MOUSEBUTTONDOWN:
                    if game.mouse.get_pressed()[0]:             #9
                        game.mixer.music.play()
                        o.circle_position9=(320,320)
                        circle_combinations.append(o.circle_position9) 
                        updated_combinations.append((320,320))
                        if len(updated_combinations)==9:
                            nonecomb()
                            game_over()
                            game_quit=True  
            # from here the cross starts 
             
            if (55 < mx < 180) and (54 < my < 180):
                if event.type == game.MOUSEBUTTONDOWN:
                    if game.mouse.get_pressed()[2]:             #1
                        # Update circle position
                        game.mixer.music.play()
                        cc.cross_position1 = (58,56)
                        cross_combinations.append(cc.cross_position1)
                        updated_combinations.append((58,56))
                        if len(updated_combinations)==9:
                            nonecomb()
                            game_over()
                            game_quit=True
            if((180 < mx <310) and (55 < my < 180)):
                if event.type==game.MOUSEBUTTONDOWN:
                    if game.mouse.get_pressed()[2]:             #2
                        game.mixer.music.play()
                        # update the cross position
                        cc.cross_position2=(185,56)
                        cross_combinations.append(cc.cross_position2)
                        updated_combinations.append((185,56))
                        if len(updated_combinations)==9:
                            nonecomb()
                            game_over()
                            game_quit=True
            if((310 < mx < 435) and (55 < my < 180)):
                if event.type==game.MOUSEBUTTONDOWN:            #3
                    if game.mouse.get_pressed()[2]:
                        game.mixer.music.play()
                        cc.cross_position3=(310,56)
                        cross_combinations.append(cc.cross_position3)
                        updated_combinations.append((310,56))
                        if len(updated_combinations)==9:
                            nonecomb()
                            game_over()
                            game_quit=True
            if((55 < mx < 180) and (180 < my < 310)):
                if event.type==game.MOUSEBUTTONDOWN:
                    if game.mouse.get_pressed()[2]:             #4
                        game.mixer.music.play()
                        cc.cross_position4=(58,188)
                        cross_combinations.append(cc.cross_position4)
                        updated_combinations.append((58,188))
                        if len(updated_combinations)==9:
                            nonecomb()
                            game_over()
                            game_quit=True
            if((180 < mx <310) and (180 < my < 310)):
                if event.type==game.MOUSEBUTTONDOWN:
                    if game.mouse.get_pressed()[2]:             #5
                        game.mixer.music.play()
                        cc.cross_position5=(185,188) 
                        cross_combinations.append(cc.cross_position5)
                        updated_combinations.append((185,188) )
                        if len(updated_combinations)==9:
                            nonecomb()
                            game_over()
                            game_quit=True
            if((310 < mx < 435) and (180 < my < 310)):
                if event.type==game.MOUSEBUTTONDOWN:
                    if game.mouse.get_pressed()[2]:             #6
                        game.mixer.music.play()
                        cc.cross_position6=(310,188) 
                        cross_combinations.append(cc.cross_position6)
                        updated_combinations.append((310,188) )
                        if len(updated_combinations)==9:
                            nonecomb()
                            game_over()
                            game_quit=True    
            if((55 < mx < 180) and (310 < my < 435)):
                if event.type==game.MOUSEBUTTONDOWN:
                    if game.mouse.get_pressed()[2]:             #7
                        game.mixer.music.play()
                        cc.cross_position7=(58,320)
                        cross_combinations.append(cc.cross_position7) 
                        updated_combinations.append((58,320))
                        if len(updated_combinations)==9:
                            nonecomb()
                            game_over()
                            game_quit=True 
            if((180 < mx <310) and (310 < my < 435)):
                if event.type==game.MOUSEBUTTONDOWN:
                    if game.mouse.get_pressed()[2]:             #8
                        game.mixer.music.play()
                        cc.cross_position8=(190,320)
                        cross_combinations.append(cc.cross_position8)
                        updated_combinations.append((190,320))
                        if len(updated_combinations)==9:
                            nonecomb()
                            game_over()
                            game_quit=True
            if((310 < mx < 435) and (310 < my < 435)):
                if event.type==game.MOUSEBUTTONDOWN:
                    if game.mouse.get_pressed()[2]:
                        cc.cross_position9=(320,320)            #9
                        game.mixer.music.play()
                        cross_combinations.append(cc.cross_position9)
                        updated_combinations.append((320,320))
                        if len(updated_combinations)==9:
                            nonecomb()
                            game_over()
                            game_quit=True                      
        # Draw circle if position is not None
        # this is of circle
        if o.circle_position1 is not None:
            gamewindow.blit(oimg,(58,56))
            
        if o.circle_position2 is not None:
            gamewindow.blit(oimg,(185,56))
            
        if o.circle_position3 is not None:
            gamewindow.blit(oimg,(310,56))
        
        if o.circle_position4 is not None:
            gamewindow.blit(oimg,(58,188))
            
        if o.circle_position5 is not None:
            gamewindow.blit(oimg,(185,188))
            
        if o.circle_position6 is not None:
            gamewindow.blit(oimg,(310,188))
            
        if o.circle_position7 is not None:
            gamewindow.blit(oimg,(58,320))
        
        if o.circle_position8 is not None:
            gamewindow.blit(oimg,(190,320))  
        
        if o.circle_position9 is not None:
            gamewindow.blit(oimg,(320,320))
        
        # this is of cross
        
        if cc.cross_position1 is not None:
            gamewindow.blit(ximg,(58,56))
            
        if cc.cross_position2 is not None:
            gamewindow.blit(ximg,(185,56))
            
        if cc.cross_position3 is not None:
            gamewindow.blit(ximg,(310,56))
        
        if cc.cross_position4 is not None:
            gamewindow.blit(ximg,(58,188))
            
        if cc.cross_position5 is not None:
            gamewindow.blit(ximg,(185,188))
            
        if cc.cross_position6 is not None:
            gamewindow.blit(ximg,(310,188))
            
        if cc.cross_position7 is not None:
            gamewindow.blit(ximg,(58,320))
        
        if cc.cross_position8 is not None:
            gamewindow.blit(ximg,(190,320))  
        
        if cc.cross_position9 is not None:
            gamewindow.blit(ximg,(320,320))
        
        if check_winner(circle_combinations):
            score = int(read) + 10
            with open('score1.txt', 'w') as f:
                f.write(str(score))
            nonecomb()
            for i in range(5):
                game_over()
        elif check_winner(cross_combinations):
            score1=int(read1)+10
            with open('score2.txt','w') as f:
                f.write(str(score1))
            nonecomb()
            for i in range(5):
                game_over()  
        update()
        clock.tick(fps)
    game.quit()
    quit()
gameloop()