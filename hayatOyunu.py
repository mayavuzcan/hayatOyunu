# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 02:07:32 2019

@author: mayav
"""
import os
import time
import sys
import random

class Evren(object):
   def __init__(self,w,h):
        self.w=w
        self.h=h 
        self.contents ={}
        self.olusturma = 0
        for y in range(self.h):
            for x in range(self.w):
                self.contents[x,y]=0
                
        
       
            
   def rastgele(self):
        cikis={}
        self.olusturma = 1
        for y in range(self.h):
            for x in range(self.w):
                c = random.randint(0, 1)
                if c==0:
                    cikis[x,y]=1
                else:
                    cikis[x,y]=0
        
        self.contents =cikis
        
   def getString(self):
        toString=" "
        for y in range(self.h):
            for x in range(self.w):
                c = self.contents[x,y]
                
                if c == 0:
                    toString +=" "
                elif c == 1:
                    toString +=u"\u2588"
            toString += "\n"
        return toString
   def hesaplama(self):
       yeni={}
       for y in range(self.h):
            for x in range(self.w):
                c = self.contents[x,y]
                u, d, l, r, ur, ul, dr, dl = self.getKomsu(x,y)
                n = [u, d, l, r, ur, ul, dr, dl]
                n = self.KomsuSayisi(n)
                if c == 1:
                    if n > 3:
                        yeni[x,y] = 0
                    elif n < 2:
                        yeni[x,y] = 0
                    elif n == 2 or n == 3:
                        yeni[x,y]=1
                elif c==0:
                    if n == 3:
                        yeni[x,y]=1
                    else:
                        yeni[x,y]=0
       self.contents=yeni               

   def getKomsu(self,x,y):  
        c=self.contents
        try: u = c[x,y-1]
        except: u = 0
        try: d = c[x,y+1]
        except: d = 0
        try: l = c[x-1,y]
        except: l = 0
        try: r = c[x+1,y]
        except:r = 0

        try: ur = c[x+1,y-1]
        except: ur = 0
        try: ul = c[x-1,y-1]
        except: ul = 0
        try: dr = c[x+1,y+1]
        except: dr = 0
        try: dl= c[x-1,y+1]
        except: dl = 0

        return u, d, l, r, ur, ul, dr, dl


   def KomsuSayisi(self,n):
       sayi=0
       for i in range(len(n)):
           c=n[i]
           if c == 1:
               sayi += 1
       return sayi
    
def tmz():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("temiz")

try:
        GENISLIK=int(sys.argv[1])
except:
        GENISLIK=100
try:
        YUKSEKLIK=int(sys.argv[2])
except:
        YUKSEKLIK=12

try:
        DELAY=float(sys.argv[3])
except:
        DELAY=0.1
        
evren = Evren(GENISLIK, YUKSEKLIK)
evren.rastgele()

while True:
    evren.hesaplama()
    tmz()
    print(evren.getString())
    time.sleep(DELAY)
