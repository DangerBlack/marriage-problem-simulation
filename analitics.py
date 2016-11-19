import numpy as np
import matplotlib.pyplot as plt
import datetime

from people import People
from peopleManager import PeopleManager
from environment import *

class Analitics:

    def correlationWinnerEgo(self,winner,pm):
        passed = 0
        for i in range(0,len(pm.people)/5):
            if pm.people[winner[i][1]].egoMax >= MAX_LIKE_LEVEL - MAX_LIKE_LEVEL/5:
                passed = passed + 1
        print("dbg e a: "+str(passed))
        if passed > (len(pm.people)/5) - (len(pm.people)/5)/5:
            return True
        else:
            return False

    def correlationWinnerEgoLow(self,winner,pm):
        passed = 0
        for i in range(0,len(pm.people)/5):
            if pm.people[winner[i][1]].egoMax <= MAX_LIKE_LEVEL/5:
                passed = passed + 1
        print("dbg e l: "+str(passed))
        if passed > (len(pm.people)/5) - (len(pm.people)/5)/5:
            return True
        else:
            return False

    def correlationWinnerInit(self,winner,pm):
        passed = 0
        for i in range(0,len(pm.people)/5):
            if pm.people[winner[i][1]].initMax >= MAX_LIKE_LEVEL - MAX_LIKE_LEVEL/5:
                passed = passed + 1
        print("dbg i a: "+str(passed))
        if passed > (len(pm.people)/5) - (len(pm.people)/5)/5:
            return True
        else:
            return False

    def correlationWinnerInitLow(self,winner,pm):
        passed = 0
        for i in range(0,len(pm.people)/5):
            if pm.people[winner[i][1]].initMax <= MAX_LIKE_LEVEL/5:
                passed = passed + 1
        print("dbg i l: "+str(passed))
        if passed > (len(pm.people)/5) - (len(pm.people)/5)/5:
            return True
        else:
            return False

    def correlationWinnerEgoInitLow(self,winner,pm):
        passed = 0
        for i in range(0,len(pm.people)/5):
            if pm.people[winner[i][1]].initMax*pm.people[winner[i][1]].egoMax <= MAX_LIKE_LEVEL*MAX_LIKE_LEVEL/5:
                passed = passed + 1
        print("dbg e*i l: "+str(passed))
        if passed > (len(pm.people)/5) - (len(pm.people)/5)/5:
            return True
        else:
            return False

    def correlationWinnerEgoInit(self,winner,pm):
        passed = 0
        for i in range(0,len(pm.people)/5):
            if pm.people[winner[i][1]].initMax*pm.people[winner[i][1]].egoMax >= MAX_LIKE_LEVEL*MAX_LIKE_LEVEL - MAX_LIKE_LEVEL*MAX_LIKE_LEVEL/5:
                passed = passed + 1
        print("dbg e*i a: "+str(passed))
        if passed > (len(pm.people)/5) - (len(pm.people)/5)/5:
            return True
        else:
            return False

    def correlationWinnerNice(self,winner,pm):
        passed = 0
        top_beauty = 0
        for p in pm.people:
            if p.nice > top_beauty:
                top_beauty = p.nice

        for i in range(0,len(pm.people)/5):
            if pm.people[winner[i][1]].nice >= top_beauty - top_beauty/5:
                passed = passed + 1
        print("dbg beauty: "+str(passed)+" "+str(top_beauty))
        if passed > (len(pm.people)/5) - (len(pm.people)/5)/5:
            return True
        else:
            return False

    def plotCoupleMonth(self,month,coupleMonth):
        global PATH
        x = [i for i in range(0,len(coupleMonth))]
        plt.title('Number of couple each month')
        plt.ylabel('month of fun')
        plt.xlabel('people')
        a = plt.plot(x,coupleMonth,label="# couple")
        plt.legend(loc=4)
        plt.savefig(PATH+str(len(coupleMonth))+"month_ncouple.png")
        plt.close()

    def plotCorrelation(self,winner,pm):
        global PATH
        yego = []
        yinit = []
        for i in range(0,len(pm.people)/5):
            p=pm.people[winner[i][1]]
            yego.append(p.egoMax)
            yinit.append(p.initMax)
        plt.title('Ego and Init')
        plt.ylabel('Initiative')
        plt.xlabel('Ego')
        d = plt.scatter(yego,yinit, label = "init")
        plt.legend()
        plt.savefig(PATH+str(MAX_LIKE_LEVEL)+"like_egoxinit_correlation.png")
        plt.close()

    def plotYearOfFun(self,pm):
        global PATH
        x = []
        ymax = []
        ysum = []
        ynice = []
        yego = []
        yinit = []
        for p in pm.people:
            try:
                #print("aggiungo "+str(p.id))
                x.append(p.id)
                ynice.append(p.nice)
                yego.append(p.egoMax*10)
                yinit.append(p.initMax*10)
                ymax.append( max(p.yearOfFun) )
                ysum.append( sum(p.yearOfFun) )
            except:
                print("errore")

        plt.title('Max year of fun')
        plt.ylabel('month of fun')
        plt.xlabel('people')
        a = plt.plot(x,ymax,label="max mof")
        b = plt.plot(x,ynice,label = "nice")
        c = plt.plot(x,yego,label = "ego")
        d = plt.plot(x,yinit, label = "init")
        plt.legend()
        plt.savefig(PATH+str(len(pm.people))+"ppl_max_monthoffun.png")
        plt.close()

        plt.title('Summed year of fun')
        plt.ylabel('month of fun')
        plt.xlabel('people')
        plt.plot(x,ysum)
        plt.savefig(PATH+str(len(pm.people))+"ppl_sum_monthoffun.png")
        plt.close()
