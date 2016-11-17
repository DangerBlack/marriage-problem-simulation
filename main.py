#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random as r

from people import People
from peopleManager import PeopleManager
from simulationCore import SimulationCore
from analitics import Analitics

r.seed(123456) #dbg purpose
#p = People(0,r.randint(0,10),r.randint(0,10),r.randint(0,1))
#print(p)


#pm = PeopleManager(100)
#for i in range(0,len(pm.people)):
#    print(pm.people[i])

sm = SimulationCore(100,60)

sm.runSimulation()
print(sm.pm)

print("--------------------------------------------------------------------")
print("SHAME LIST")
for p in sm.pm.people:
    if not p.isEngaged():
        print(p)
        print("N partner: "+str(len(p.partnerList)))
        #print(p.partnerList)
        print("Mesi di divertimento: "+str(sum(p.yearOfFun)))
        #print(p.yearOfFun)
        #print(p.like)
        print("--------------------------------------------------------------------")


print("WINNER LIST ~ LONG WEDDING")
winner =[]
for p in sm.pm.people:
    if p.isEngaged():
        winner.append([max(p.yearOfFun),p.id])

winner.sort(key=lambda x: x[0],reverse=True)

for i in range(0,20):
    print(str(winner[i][1])+" fidanzato per: "+str(int(winner[i][0]/12))+" anni")
    print(sm.pm.people[winner[i][1]])
    print("N partner: "+str(len(p.partnerList)))
    print("Mesi di divertimento: "+str(sum(p.yearOfFun)))
    print("--------------------------------------------------------------------")

a = Analitics()

a.plotYearOfFun(sm.pm)
