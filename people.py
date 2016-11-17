#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random as r

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
        for i in range(0,len(self.like)):
            if(self.like[i] == 0):
                self.like[i] = r.randint(0,10)

    def isEngaged(self):
        if(self.engaged != -1):
            return True
        else:
            return False

    def incEgoR(self):
        if self.ego<10 and r.randint(0,100)>80:
            self.ego = self.ego + 1
        if self.ego > 10:
            self.ego = 10

    def incEgo(self,b):
        if self.ego<10 and r.randint(0,100)>80:
            dif = self.like[b.id]-self.ego
            dif = max(1,dif)
            self.ego = self.ego + r.randint(0,dif)
        if self.ego > 10:
            self.ego = 10

    def incInit(self):
        if self.init<10 and r.randint(0,100)>80:
            self.init = self.init + 1

    def decEgo(self,prob):
        if self.ego>0 and r.randint(0,100)>prob:
            self.ego = self.ego - 1

    def decInit(self):
        if self.init>0 and r.randint(0,100)>80:
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
        if self.accept(b):
            if b.accept(self):
                self.incEgo(b)
                b.incEgo(self)
                self.pendingOffer.append(b.id)
                b.pendingOffer.append(self.id)
            else:
                b.incEgo(self)
                self.decEgo(70)
        else:
            pass


    def __str__(self):
        return "["+str(self.id)+"] sex: "+str(self.sex)+" ego: "+str(self.ego)+"/"+str(self.egoMax)+" init: "+str(self.init)+"/"+str(self.initMax)+" nice: "+str(self.nice)+" partner: "+str(self.engaged)+" RIP?:"+str(self.deadTick)
