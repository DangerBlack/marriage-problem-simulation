#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random as r
from environment import *

class People:

    #@id a progressive number
    #@egoMax self confidence, you refuse parner avance you like less then your ego,
    #@initMaz pushing beahavior, how hard you try, number of try each month
    #@sex 0 male, 1 female
    def __init__(self,id,egoMax,initMax,sex):
        self.id = id
        self.egoMax = egoMax
        self.initMax = initMax
        self.ego = egoMax
        self.init = initMax
        self.like = []
        self.nice = 0
        self.sex = sex
        self.lastRelation = -1
        self.engaged = -1
        self.pendingOffer = []
        self.deadTick = r.randint(35*12,90*12)

        self.yearOfFun = []
        self.partnerList = []

    def initLike0(self,n):
        self.like=[0] * n

    def initUndefinedLike(self):
        global MAX_LIKE_LEVEL
        for i in range(0,len(self.like)):
            if(self.like[i] == 0):
                self.like[i] = r.randint(0,MAX_LIKE_LEVEL)

    def isEngaged(self):
        if(self.engaged != -1):
            return True
        else:
            return False

    def incEgoR(self):
        global INC_EGO_PROBABILTY_RANDOM
        global MAX_LIKE_LEVEL
        if self.ego<MAX_LIKE_LEVEL and r.randint(0,100)>INC_EGO_PROBABILTY_RANDOM:
            self.ego = self.ego + 1
        if self.ego > MAX_LIKE_LEVEL:
            self.ego = MAX_LIKE_LEVEL

    def incEgo(self,b):
        global INC_EGO_PROBABILTY_B
        if self.ego<MAX_LIKE_LEVEL and r.randint(0,100)>INC_EGO_PROBABILTY_B:
            dif = self.like[b.id]-self.ego
            dif = max(1,dif)
            self.ego = self.ego + r.randint(0,dif)
        if self.ego > MAX_LIKE_LEVEL:
            self.ego = MAX_LIKE_LEVEL

    def incInit(self):
        global INC_INIT
        global MAX_LIKE_LEVEL
        if self.init<MAX_LIKE_LEVEL and r.randint(0,100)>INC_INIT:
            self.init = self.init + 1

    def decEgo(self,prob):
        if self.ego>0 and r.randint(0,100)>prob:
            self.ego = self.ego - 1

    def decInit(self):
        global DEC_INIT
        if self.init>0 and r.randint(0,100)>DEC_INIT:
            self.init = self.init - 1

    def accept(self,b):
        if self.ego <= self.like[b.id]:
            #mi piace
            if(not self.isEngaged()):
                #mi piace e sono single
                return True
            if self.init >= r.randint(0,10):
                #mi piace sono findanzato ma ho voglia di cambiare
                return True;
            else:
                #mi piace sono fidanzato ma sto bene qui
                return False;
        else:
            #non mi piace
            return False

    def meet(self,b):
        global DEC_EGO_NOT_ACCEPTED
        if self.accept(b):
            if b.accept(self):
                self.incEgo(b)
                b.incEgo(self)
                self.pendingOffer.append(b.id)
                b.pendingOffer.append(self.id)
            else:
                b.incEgo(self)
                self.decEgo(DEC_EGO_NOT_ACCEPTED)
        else:
            pass


    def __str__(self):
        if(len(self.yearOfFun)==0):
            self.yearOfFun.append(0)
        return "["+str(self.id)+"] sex: "+str(self.sex)+"\tego: "+str(self.ego)+"/"+str(self.egoMax)+"\tinit: "+str(self.init)+"/"+str(self.initMax)+"\tnice: "+str(self.nice)+"\ttaste: "+str(sum(self.like)/len(self.like))+"\tpartner: "+str(self.engaged)+"\tRIP-in: "+str(self.deadTick)+"\tlongest-rel:"+str(max(self.yearOfFun))
