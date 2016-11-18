#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random as r

from people import People
from environment import *

class PeopleManager:

    def __init__(self,n):
        global MAX_LIKE_LEVEL
        self.egoMax = MAX_LIKE_LEVEL
        self.initMax = MAX_LIKE_LEVEL
        self.n = n;
        self.people = []
        self.initPeople(n)

    def initPeople(self,n):
        global MAX_LIKE_LEVEL
        #(self,id,egoMax,initMax,sex):
        ncore = 10 # n/10
        for i in range(0,n):
            p = People(i,r.randint(0,self.egoMax),r.randint(0,self.initMax),r.randint(0,1))
            p.initLike0(n)
            if(len(self.people)>0):
                for j in range(0,min(ncore,len(self.people))):
                    lover = r.randint(0,len(self.people)-1)
                    p.like[lover] = r.randint(MAX_LIKE_LEVEL-MAX_LIKE_LEVEL/20,MAX_LIKE_LEVEL)
                    self.people[lover].nice = self.people[lover].nice + p.like[lover]
            p.initUndefinedLike()
            self.people.append(p);

    def getMatingPartner(self,p,tick):#non frequento gente morta
        idx = r.randint(0,len(self.people)-1)
        q = self.people[idx]
        while q.id == p.id or q.sex == p.sex or q.deadTick < tick or (r.randint(0,10)>2 and q.isEngaged()):
            idx = r.randint(0,len(self.people)-1)
            q = self.people[idx]
        return q

    def __str__(self):
        s =""
        for p in self.people:
            s=s+str(p)+"\n"
        return s

    def printCouple(self):
        for p in self.people:
            if( p.isEngaged()):
                print(str(p.id)+" <-> "+str(p.engaged)+" happyness: "+str(p.ego))
