from math import *
from kandinsky import *
from ion import * 
from random import * 
from time import * 

print("play1v1()")
print("play1vmur()")

def initialisationDuFichierAnnexe():                  #utilisable qu'avec Omega
  FHighScore=open("highscore.py","w")                 #utilisable qu'avec Omega
  FHighScore.write("10")                              #utilisable qu'avec Omega

bluescore=0
redscore=0

def initialisation():
  global murscore, endloop, y1, y2, xballe, yballe, incrementx, incrementy
  murscore=0
  endloop=0
  y1=100
  y2=100
  xballe=150
  yballe=115
  Random=[-1,1]
  incrementx=choice(Random)
  incrementy=randint(-1,1)

def raquette1():
  global y1
  if keydown(KEY_SEVEN):
    fill_rect(5,y1,5,50,color(255,255,255))
    y1-=3
    fill_rect(5,y1,5,50,color(255,0,0))
  if keydown(KEY_ZERO):
    fill_rect(5,y1,5,50,color(255,255,255))
    y1+=3
    fill_rect(5,y1,5,50,color(255,0,0))

def raquette2(couleur):
  global y2
  if keydown(KEY_RIGHTPARENTHESIS):
    if couleur=="blanc":
      fill_rect(310,y2,5,50,color(255,255,255))
    elif couleur=="noir":
      fill_rect(310,y2,5,50,color(0,0,0))
    y2-=3
    fill_rect(310,y2,5,50,color(0,0,255))
  if keydown (KEY_EXE):
    if couleur=="blanc":
      fill_rect(310,y2,5,50,color(255,255,255))
    elif couleur=="noir":
      fill_rect(310,y2,5,50,color(0,0,0))
    y2+=3
    fill_rect(310,y2,5,50,color(0,0,255))

def balle(couleur):
  global xballe, yballe
  if couleur=="blanc":
    fill_rect(xballe,yballe,10,10,color(255,255,255))
  elif couleur=="noir":
    fill_rect(xballe,yballe,10,10,color(0,0,0))
  xballe+=incrementx
  yballe+=incrementy
  fill_rect(xballe,yballe,10,10,color(255,255,0))

def reboundtest():
  global incrementx, incrementy
  xtest=xballe-5
  ytest=yballe
  for i in range(2):
    for i in range(2):
      if get_pixel(xtest,ytest)==color(0,0,255):
        incrementx=-3
        incrementy=randint(-1,1)
      if get_pixel(xtest,ytest)==color(255,0,0):
        incrementx=3
        incrementy=randint(-1,1)
      ytest+=10
    xtest+=20
    ytest=yballe 

def bordertest():
  global incrementy
  if yballe<=0:
    incrementy=1
  if yballe+10>=221:
    incrementy=-1

def fautetest():
  global bluescore, redscore, endloop
  if xballe<=0:
    bluescore+=1
    if bluescore<3:
      play1v1()
    elif bluescore==3:
      endloop=1
  if xballe>=350:
    redscore+=1
    if redscore<3:
      play1v1()
    elif redscore==3:
      endloop=1
      
def play1v1():
  global bluescore, redscore
  fill_rect(0,0,350,222,color(255,255,255))
  initialisation()
  draw_string("Bluescore : "+str(bluescore),5,5)
  draw_string("Redscore : " +str(redscore),190,5)
  fill_rect(xballe,yballe,10,10,color(255,255,0))
  fill_rect(5,y1,5,50,color(255,0,0))
  fill_rect(310,y2,5,50,color(0,0,255))
  sleep(3)
  fill_rect(0,0,350,50,color(255,255,255))
  while endloop==0:
    raquette1()
    raquette2("blanc")
    balle("blanc")
    reboundtest() 
    bordertest()
    fautetest()
  if bluescore==3:
    draw_string("Le bleu a gagné !" ,85,80)
    draw_string("OK pour la revanche",70,120)
  if redscore==3:
    draw_string("Le rouge a gagné !",80,80)
    draw_string ("OK pour la revanche",70,120)
  while True:
    if keydown(KEY_OK):
      bluescore=0 
      redscore=0
      play1v1()
    if keydown(KEY_BACKSPACE):
      return
          
def reboundtestmur():
  global incrementx, incrementy, murscore
  xtest=xballe-5
  ytest=yballe
  for i in range(2):
    for i in range(2):
      if get_pixel(xtest,ytest)==color(0,0,255):
        if incrementx!=-3:
          murscore+=1
        incrementx=-2
        incrementy=randint(-1,1)
      elif xtest<=0:
        incrementx=2
        incrementy=randint(-1,1)
      ytest+=10
    ytest=yballe
    xtest+=20

def fautetestmur():
  global endloop
  if xballe>=350:
    fill_rect(0,0,350,250,color(255,255,255))
    endloop=1

def play1vmur():
  FHighScore=open("highscore.py","r")                   #utilisable qu'avec Omega
  HighScore=FHighScore.read(2)                          #utilisable qu'avec Omega
  FHighScore.close                                      #utilisable qu'avec Omega
  initialisation()
  fill_rect(0,0,350,222,color(0,0,0))
  fill_rect(xballe,yballe,10,10,color(255,255,0))
  fill_rect(310,y2,5,50,color(0,0,255))
  sleep(3)
  while endloop==0:
    raquette2("noir")
    balle("noir")
    bordertest()
    reboundtestmur()
    fautetestmur()
  if murscore>int(HighScore):                             #utilisable qu'avec Omega
    HighScore=murscore                                    #utilisable qu'avec Omega
    draw_string("Nouveau record: "+str(HighScore),75,100) #utilisable qu'avec Omega
    FHighScore=open("highscore.py","w")                   #utilisable qu'avec Omega
    FHighScore.write(str(HighScore))                      #utilisable qu'avec Omega
  elif murscore<10:
    draw_string("Ton score est de "+str(murscore)+" (cheh)",45,80)
    draw_string("Record actuel: "+str(HighScore),75,150)  #utilisable qu'avec Omega
  elif murscore>=10:
    draw_string("Ton score est de "+str(murscore)+" bravo !",35,80)
    draw_string("Record actuel : "+str(HighScore),75,120)  #utilisable qu'avec Omega
  while True:
    if keydown(KEY_OK):
      bluescore=0
      redscore=0
      play1vmur()
    if keydown(KEY_BACKSPACE):
      return
