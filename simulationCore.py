#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random as r

from people import People
from peopleManager import PeopleManager
from environment import *

class SimulationCore:
    def __init__(self,n,year):
        self.pm = PeopleManager(n)
        self.tick = 0
        self.end = year*12


    def runSimulation(self):
        for i in range(1,self.end):
            self.simulationTick(i)
            self.logInfo(i)
            #print(self.pm)



    def simulationTick(self,tick):
        global DEC_EGO_CRONICAL_SINGLE
        global DEC_EGO_CRONICAL_SINGLE_2
        for p in self.pm.people:
            for i in range(0,3+p.init*2):
                q = self.pm.getMatingPartner(p,tick)
                p.meet(q)

        for p in self.pm.people:
            if len(p.pendingOffer)>0:
                q = self.pm.people[p.pendingOffer[0]]
                if p.id in q.pendingOffer:
                    q.pendingOffer = []
                    if q.isEngaged:
                        if self.pm.people[q.engaged].engaged == q.id:
                            self.pm.people[q.engaged].engaged = -1 #dico a lui che ora è single
                            old = self.pm.people[q.engaged]
                        else:
                            print("lui non sta con me "+str(q.id)+" "+str(self.pm.people[q.engaged].id))
                    if p.isEngaged:
                        old = self.pm.people[p.engaged]
                        old.engaged = -1 #dico a lui che ora è single
                    q.engaged = p.id
                    p.engaged = q.id
                    p.pendingOffer = []
                    p.lastRelation = tick
                    q.lastRelation = tick
                    p.partnerList.append(q.id)
                    p.yearOfFun.append(0)
                    q.partnerList.append(p.id)
                    q.yearOfFun.append(0)


        for p in self.pm.people:
            if p.isEngaged():
                p.yearOfFun[-1]=p.yearOfFun[-1] + 1

            if not p.isEngaged() and p.ego < p.egoMax: #sono single ma sono forte
                p.incEgoR()

            if not p.isEngaged() and p.init < p.initMax: #sono single ed amo provarci ma esco da una brutta storia
                p.incInit()

            if not p.isEngaged() and ((tick - p.lastRelation) %  6) == 0: #piu di sei mesi che non frequenti ragazze/i
                p.decEgo(DEC_EGO_CRONICAL_SINGLE)
                p.decEgo(DEC_EGO_CRONICAL_SINGLE_2)
            else:
                if p.isEngaged() and ((tick - p.lastRelation) %  6) == 0: #più di sei mesi che stai con la stessa/o
                    p.decInit()
                    p.incEgo(self.pm.people[p.engaged])

        print("                  "+str(tick)+" month")
        self.pm.printCouple()

    def logInfo(self,tick):
        single = 0
        alive = 0
        for p in self.pm.people:
            if int(p.deadTick) > int(tick):
                alive = alive + 1
                if not p.isEngaged():
                    single = single +1

        print('Number of single : '+str(single)+" / "+str(alive))
