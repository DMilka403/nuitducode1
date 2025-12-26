import pyxel
import time

start = False
stop = False
finish = False
porte1 = False
porte2 = True
porte3 = True
premier = False
second = False
troisieme = False

x_perso = 40
y_perso = 40
direction = 'fixe'
mouvement = 1

x_porte1 = [i for i in range(-60,0)]
y_porte1 = -6 

x_porte2 = [i for i in range(-116,-56)]
y_porte2 = -124 

x_porte3 = [i for i in range(4,64)]
y_porte3 = -124

pyxel.init(128, 128, title="Nuit du Code")
pyxel.load("theme2.pyxres")

def est_murgauche(x,y):
    if x < -60 and -60 < y < 108:
        return True
    if x < -116 and -184 < y < -76:
        return True
    if 0< x < 4 and -124 < y < -8:
        return True
    
    return False

def est_murdroit(x,y):
    if 102>x > 108 and 4<y<108:
        return True
    if -12 > x > -16 and -118<y<-14:
        return True
    if x > 48 and -184<y<-16:
        return True
    
    return False

def est_murhaut(x,y):
    
    if -116 < x < 48 and y < -184:
        return True
    if -70 < x < -16 and -116 < y < -120:
        return True
    if 0 < x < 108 and 2<y < 6:
        return True
    return False

def est_murbas(x,y):
    if -60 < x < 108 and y > 108:
        return True
    if -116 < x < -72 and y > -76:
        return True
    if -72 < x < -10 and -136 > y > -140:
        return True

    if 2 < x < 50 and -20 > y > -16:
        return True
    return False


def update():
    global x_perso,y_perso, direction, start, stop, porte1,porte2,porte3,premier,second,troisieme, finish
    direction = 'fixe'
    if pyxel.btn(pyxel.KEY_ESCAPE):
        exit()
    if (pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_KP_6)) and not est_murdroit(x_perso,y_perso)  :
        direction = 'right'
        x_perso += 2
    if (pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_KP_4)) and not est_murgauche(x_perso,y_perso)  :
        direction = 'left'
        x_perso -= 2
    if (pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_KP_8))  and not est_murhaut(x_perso,y_perso) :
        direction = 'up' 
        y_perso -= 2
    if (pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_KP_2)) and not est_murbas(x_perso,y_perso)  :
        direction = 'down'
        y_perso += 2
    if pyxel.btn(pyxel.KEY_SPACE) and start == False:
        start = True

    if y_perso == y_porte1 and x_perso in x_porte1 and porte1 == False:
        stop = True
        premier = True  
        porte1 = True
        porte2 = False
    if pyxel.btn(pyxel.KEY_9):
        stop = False
        premier = False

    if y_perso == y_porte2 and x_perso in x_porte2 and porte2 == False:
        stop = True
        second = True
        porte2 = True
        porte3 = False
        if pyxel.btn(pyxel.KEY_8):
            stop = False
            second = False

    if y_perso == y_porte3 and x_perso in x_porte3 and porte3 == False:
        stop = True
        troisieme = True
        porte3 = True
        if pyxel.btn(pyxel.KEY_6):
            stop = False
            troisieme = False

    if y_perso == -60 and x_perso in [i for i in range(24,48)]:
        finish = True


    pyxel.camera(x_perso - 56, y_perso - 56)


def draw():
    global start, stop, premier,second,troisieme, mouvement
    if stop != True:
        if start != False :
            pyxel.cls(0)
            pyxel.rect(0,0,128,4,9)
            pyxel.rect(124,4,4,120,9)
            pyxel.rect(-60,124,188,4,9)
            pyxel.rect(-64,-60,4,188,9)
            pyxel.rect(0,-124,4,124,9)
            pyxel.rect(-120,-60,56,4,9) 
            pyxel.rect(-120,-184,4,124,9)
            pyxel.rect(-70,-124,70,4,9)
            pyxel.rect(-120,-188,192,4,9)
            pyxel.rect(64,-184,4,184,9)
            if porte1 == False :
                pyxel.blt(-60,-6,0,48,0,60,16)
            if porte2 == False :   
                pyxel.blt(-116,-124,0,0,32,80,8)
            if porte3 == False :    
                pyxel.blt(10,-124,0,0,40,53,16)
            if direction == 'fixe':
                pyxel.blt(x_perso,y_perso,0,0,0,16,16)
            if direction == 'right':
                if mouvement == 1:
                    pyxel.blt(x_perso,y_perso,0,16,0,16,16)
                    mouvement = 2
                else:
                    pyxel.blt(x_perso,y_perso,0,32,0,16,16)
                    mouvement = 1
            if direction == 'left':
                if mouvement == 1:
                    pyxel.blt(x_perso,y_perso,0,0,16,16,16)
                    mouvement = 2
                else:
                    pyxel.blt(x_perso,y_perso,0,16,16,16,16)
                    mouvement = 1
            if direction == 'up':
                pyxel.blt(x_perso,y_perso,0,32,0,16,16)
            if direction == 'down':
                pyxel.blt(x_perso,y_perso,0,32,0,16,16)
            pyxel.blt(24,-60,0,0,56,24,16)
        else:
            pyxel.cls(0)
            pyxel.text(16,40,"Hoganis est perdu !", 7)
            pyxel.text(16,50,"Appuyez sur Espace", 7)
    else:
        pyxel.cls(0)
        if premier == True :
            pyxel.text(x_perso-10,y_perso,"9 x 1 = ?", 7)
        elif second == True :
            pyxel.text(x_perso-10,y_perso,"4 x 2 = ?", 7)
        elif troisieme == True :
            pyxel.text(x_perso-10,y_perso,"2 x 3 = ?", 7)
    if finish == True:
            pyxel.cls(0)
            pyxel.text(x_perso-50,y_perso-20,'Bravo ! Vous etes a la surface', 7)


pyxel.run(update, draw)