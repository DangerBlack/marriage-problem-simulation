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
