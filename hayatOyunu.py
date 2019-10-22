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


        for y in range(self.h):
            for x in range(self.w):
                self.contents[x,y]=0
                
        
       
            
   def rastgele(self):
        cikis={}
        for y in range(self.h):
            for x in range(self.w):
                c = random.randint(0, 30)
                if c==0:
                    cikis[x,y]=1
                else:
                    cikis[x,y]=0
        
        self.contents =cikis
        
   def getString(self):
        toString=""
        for y in range(self.h):
            for x in range(self.w):
                c=self.contents[x,y]
                
                if c==0:
                    toString +=" "
                elif c==1:
                    toString +=u"\u2588"
            toString += "\n"
        return toString

   def getKomsu(self):  
        pass
    
def tmz():
        if os.name=="nt":
            os.system("tmz")
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
        
evren = Evren(GENISLIK, YUKSEKLIK)
evren.rastgele()

while True:
    tmz()
    
    # pozisyon hesaplama 
    print(evren.getString())
