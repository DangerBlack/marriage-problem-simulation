#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random as r

from people import People
from peopleManager import PeopleManager
from simulationCore import SimulationCore

r.seed(123456) #dbg purpose
#p = People(0,r.randint(0,10),r.randint(0,10),r.randint(0,1))
#print(p)


#pm = PeopleManager(100)
#for i in range(0,len(pm.people)):
#    print(pm.people[i])

sm = SimulationCore(100,60)

sm.runSimulation()
print(sm.pm)

print("SHAME LIST")
for p in sm.pm.people:
    if not p.isEngaged():
        print(p)
        print(p.like)

print("WINNER LIST ~ LONG WEDDING")
winner =[]
for p in sm.pm.people:
    if p.isEngaged():
        winner.append([sm.end-p.lastRelation,p.id])

winner.sort(key=lambda x: x[0],reverse=True)

for i in range(0,10):
    print(str(winner[i][1])+" fidanzato da: "+str(int(winner[i][0]/12))+" anni")
    print(sm.pm.people[winner[i][1]])
