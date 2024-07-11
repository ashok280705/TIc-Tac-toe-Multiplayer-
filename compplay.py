import pygame as game
import random as r
import colours as c
import cross as cc
import circle as o

game.init()

# setting the gaming window
screenwidth=500
screenheight=500
gamewindow=game.display.set_mode((500,500))
game.display.set_caption("TIC-TAC-TAO")
clock=game.time.Clock()

# creating a font
font=game.font.SysFont(None,57)

# update function
def update():
    game.display.update()

# loading a music
game.mixer.init()
game.mixer.music.load("beep.mp3")

# loading background image
bgimg = game.image.load("tic-tac back.png")
bgimg = game.transform.scale(bgimg, (screenheight, screenwidth)).convert_alpha()

cimg = game.image.load("choice2.png")
cimg = game.transform.scale(cimg, (screenheight, screenwidth)).convert_alpha()

oimg=game.image.load('o.png')
oimg=game.transform.scale(oimg,(115,115)).convert_alpha()

ximg=game.image.load('x.png')
ximg=game.transform.scale(ximg,(115,115)).convert_alpha()

# winning combination
circle_combinations=[]
cross_combinations=[]
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

# computer_combinations
computer_combinations=[(58,56),(185,56),(310,56),(58,188),(185,188),(310,188),
                       (58,320),(190,320),(320,320)]
combination=[]
# choiceloop
def gameloop1(a,b):
    global computer_combinations
    game_quit=False
    fps=60
    while not game_quit:
        gamewindow.fill(c.white)
        gamewindow.blit(bgimg,(0,0))
        mx,my=game.mouse.get_pos()
        for event in game.event.get():
            if event.type==game.QUIT:
                game_quit=True
            match a:
                case 1:
                    if (55 < mx < 180) and (54 < my < 180):
                        if event.type == game.MOUSEBUTTONDOWN:
                            if game.mouse.get_pressed()[0]:             #1
                                 # Update circle position
                                game.mixer.music.play()
                                o.circle_position1 = (58,56)
                                circle_combinations.append(o.circle_position1)
                                index=computer_combinations.index((58,56))
                                del computer_combinations[index]
                                print(computer_combinations)
                                random_tuple = r.choice(computer_combinations)
                                combination.append(random_tuple)
                                computer_combinations.remove((random_tuple))
                                cc.cross_position11 =combination[0]
                                cross_combinations.append(cc.cross_position11)
                                
                    if((180 < mx <310) and (55 < my < 180)):
                        if event.type==game.MOUSEBUTTONDOWN:
                            if game.mouse.get_pressed()[0]:             #2
                                # update the cross position
                                game.mixer.music.play()
                                o.circle_position2=(185,56)
                                circle_combinations.append(o.circle_position2)
                                index1=computer_combinations.index((185,56))
                                del computer_combinations[index1]
                                print(computer_combinations)
                                random_tuple1 = r.choice(computer_combinations)
                                combination.append(random_tuple1)
                                computer_combinations.remove((random_tuple1))
                                cc.cross_position22 =random_tuple1
                                cross_combinations.append(cc.cross_position22)
                    if((310 < mx < 435) and (55 < my < 180)):
                        if event.type==game.MOUSEBUTTONDOWN:
                            if game.mouse.get_pressed()[0]: 
                                game.mixer.music.play()                 #3
                                o.circle_position3=(310,56)     
                                circle_combinations.append(o.circle_position3)
                                index2=computer_combinations.index((310,56))
                                del computer_combinations[index2]
                                print(computer_combinations)
                                random_tuple2 = r.choice(computer_combinations)
                                combination.append(random_tuple2)
                                computer_combinations.remove((random_tuple2))
                                cc.cross_position33 =random_tuple2
                                cross_combinations.append(cc.cross_position33) 
                    if((55 < mx < 180) and (180 < my < 310)):
                        if event.type==game.MOUSEBUTTONDOWN:
                            if game.mouse.get_pressed()[0]:             #4
                                game.mixer.music.play()
                                o.circle_position4=(58,188) 
                                circle_combinations.append(o.circle_position4)
                                index3=computer_combinations.index((58,188))
                                del computer_combinations[index3]
                                print(computer_combinations)
                                random_tuple3 = r.choice(computer_combinations)
                                combination.append(random_tuple3)
                                computer_combinations.remove((random_tuple3))
                                cc.cross_position44 =random_tuple3
                                cross_combinations.append(cc.cross_position44)
                    if((180 < mx <310) and (180 < my < 310)):
                        if event.type==game.MOUSEBUTTONDOWN:
                            if game.mouse.get_pressed()[0]:
                                game.mixer.music.play()                 #5
                                o.circle_position5=(185,188)  
                                circle_combinations.append(o.circle_position5)
                                index4=computer_combinations.index((185,188))
                                del computer_combinations[index4]
                                print(computer_combinations)
                                random_tuple4 = r.choice(computer_combinations)
                                combination.append(random_tuple4)
                                computer_combinations.remove((random_tuple4))
                                cc.cross_position55 =random_tuple4
                                cross_combinations.append(cc.cross_position55)  
                    if((310 < mx < 435) and (180 < my < 310)):
                        if event.type==game.MOUSEBUTTONDOWN:
                            if game.mouse.get_pressed()[0]:             #6
                                game.mixer.music.play()
                                o.circle_position6=(310,188) 
                                circle_combinations.append(o.circle_position6)
                                index5=computer_combinations.index((310,188))
                                del computer_combinations[index5]
                                print(computer_combinations)
                                random_tuple5= r.choice(computer_combinations)
                                combination.append(random_tuple5)
                                computer_combinations.remove((random_tuple5))
                                cc.cross_position66 =random_tuple5
                                cross_combinations.append(cc.cross_position66)
                    if((55 < mx < 180) and (310 < my < 435)):
                        if event.type==game.MOUSEBUTTONDOWN:
                            if game.mouse.get_pressed()[0]:             #7
                                game.mixer.music.play()
                                o.circle_position7=(58,320)
                                circle_combinations.append(o.circle_position7)
                                index6=computer_combinations.index((58,320))
                                del computer_combinations[index6]
                                print(computer_combinations)
                                random_tuple6 = r.choice(computer_combinations)
                                combination.append(random_tuple6)
                                computer_combinations.remove((random_tuple6))
                                cc.cross_position77 =random_tuple6
                                cross_combinations.append(cc.cross_position77)
                    if((180 < mx <310) and (310 < my < 435)):
                        if event.type==game.MOUSEBUTTONDOWN:
                            if game.mouse.get_pressed()[0]:             #8
                                game.mixer.music.play()
                                o.circle_position8=(190,320)
                                circle_combinations.append(o.circle_position8)
                                index7=computer_combinations.index((190,320))
                                del computer_combinations[index7]
                                print(computer_combinations)
                                random_tuple7 = r.choice(computer_combinations)
                                combination.append(random_tuple7)
                                computer_combinations.remove((random_tuple7))
                                cc.cross_position88 =random_tuple7
                                cross_combinations.append(cc.cross_position88)
                    if((310 < mx < 435) and (310 < my < 435)):
                        if event.type==game.MOUSEBUTTONDOWN:
                            if game.mouse.get_pressed()[0]:             #9
                                game.mixer.music.play()
                                o.circle_position9=(320,320)
                                circle_combinations.append(o.circle_position9) 
                                index8=computer_combinations.index((320,320))
                                del computer_combinations[index8]
                                print(computer_combinations)
                                random_tuple8 = r.choice(computer_combinations)
                                cc.cross_position99 =random_tuple8
                                cross_combinations.append(cc.cross_position88)     
                case 2:
                    if (55 < mx < 180) and (54 < my < 180):
                        if event.type == game.MOUSEBUTTONDOWN:
                            if game.mouse.get_pressed()[0]:             #1
                                # Update circle position
                                game.mixer.music.play()
                                cc.cross_position1 = (58,56)
                                cross_combinations.append(cc.cross_position1)
                    if((180 < mx <310) and (55 < my < 180)):
                        if event.type==game.MOUSEBUTTONDOWN:
                            if game.mouse.get_pressed()[0]:             #2
                                game.mixer.music.play()
                                # update the cross position
                                cc.cross_position2=(185,56)
                                cross_combinations.append(cc.cross_position2)
                    if((310 < mx < 435) and (55 < my < 180)):
                        if event.type==game.MOUSEBUTTONDOWN:            #3
                            if game.mouse.get_pressed()[0]:
                                game.mixer.music.play()
                                cc.cross_position3=(310,56)
                                cross_combinations.append(cc.cross_position3)
                    if((55 < mx < 180) and (180 < my < 310)):
                        if event.type==game.MOUSEBUTTONDOWN:
                            if game.mouse.get_pressed()[0]:             #4
                                game.mixer.music.play()
                                cc.cross_position4=(58,188)
                                cross_combinations.append(cc.cross_position4)
                    if((180 < mx <310) and (180 < my < 310)):
                        if event.type==game.MOUSEBUTTONDOWN:
                            if game.mouse.get_pressed()[0]:             #5
                                game.mixer.music.play()
                                cc.cross_position5=(185,188) 
                                cross_combinations.append(cc.cross_position5)
                    if((310 < mx < 435) and (180 < my < 310)):
                        if event.type==game.MOUSEBUTTONDOWN:
                            if game.mouse.get_pressed()[0]:             #6
                                game.mixer.music.play()
                                cc.cross_position6=(310,188) 
                                cross_combinations.append(cc.cross_position6)    
                    if((55 < mx < 180) and (310 < my < 435)):
                        if event.type==game.MOUSEBUTTONDOWN:
                            if game.mouse.get_pressed()[0]:             #7
                                game.mixer.music.play()
                                cc.cross_position7=(58,320)
                                cross_combinations.append(cc.cross_position7)  
                    if((180 < mx <310) and (310 < my < 435)):
                        if event.type==game.MOUSEBUTTONDOWN:
                            if game.mouse.get_pressed()[0]:             #8
                                game.mixer.music.play()
                                cc.cross_position8=(190,320)
                                cross_combinations.append(cc.cross_position8)
                    if((310 < mx < 435) and (310 < my < 435)):
                        if event.type==game.MOUSEBUTTONDOWN:
                            if game.mouse.get_pressed()[0]:
                                cc.cross_position9=(320,320)            #9
                                game.mixer.music.play()
                                cross_combinations.append(cc.cross_position9)
                                                            
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
            
        if o.circle_position11 is not None:
            gamewindow.blit(oimg,(58,56))
                        
        if o.circle_position22 is not None:
            gamewindow.blit(oimg,(185,56))
                        
        if o.circle_position33 is not None:
            gamewindow.blit(oimg,(310,56))
                    
        if o.circle_position44 is not None:
            gamewindow.blit(oimg,(58,188))
                        
        if o.circle_position55 is not None:
            gamewindow.blit(oimg,(185,188))
                        
        if o.circle_position66 is not None:
            gamewindow.blit(oimg,(310,188))
                        
        if o.circle_position77 is not None:
            gamewindow.blit(oimg,(58,320))
                    
        if o.circle_position88 is not None:
            gamewindow.blit(oimg,(190,320))  
                    
        if o.circle_position99 is not None:
            gamewindow.blit(oimg,(320,320)) 

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
            
        if cc.cross_position11 is not None:
            gamewindow.blit(ximg,random_tuple)
            
        if cc.cross_position22 is not None:
            gamewindow.blit(ximg,random_tuple1)
                        
        if cc.cross_position33 is not None:
            gamewindow.blit(ximg,random_tuple2)
                    
        if cc.cross_position44 is not None:
            gamewindow.blit(ximg,random_tuple3)
                        
        if cc.cross_position55 is not None:
            gamewindow.blit(ximg,random_tuple4)
                        
        if cc.cross_position66 is not None:
            gamewindow.blit(ximg,random_tuple5)
                        
        if cc.cross_position77 is not None:
            gamewindow.blit(ximg,random_tuple6)
                    
        if cc.cross_position88 is not None:
            gamewindow.blit(ximg,random_tuple7)  
                    
        if cc.cross_position99 is not None:
            gamewindow.blit(ximg,random_tuple8)        
        update()
        clock.tick(fps)
    game.quit()
    quit()                  
# this is the gaming loop 
def gameloop():
    game_quit=False
    fps=60
    while not game_quit:
        gamewindow.fill(c.white)
        gamewindow.blit(cimg,(0,0))
        mx, my = game.mouse.get_pos()
        for event in game.event.get():
            if event.type==game.QUIT:
                game_quit=True
            if((43 < mx <282) and (115 < my <207)):
                if event.type==game.MOUSEBUTTONDOWN:
                     if game.mouse.get_pressed()[0]:
                            print('hi')
                            a=1
                            b=1
                            gameloop1(a,b)
                            game_quit=True
                        
            if(43 < mx < 282) and (290 < my <385):
                if event.type==game.MOUSEBUTTONDOWN:
                    if game.mouse.get_pressed()[0]:
                        a=2
                        b=1
                        print('hi')
                        gameloop1(a,b)
            # print(event)
        update()
        clock.tick(fps)
    game.quit()
    quit()
gameloop()