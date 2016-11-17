import numpy as np
import matplotlib.pyplot as plt
import datetime

from people import People
from peopleManager import PeopleManager

class Analitics:

    def plotYearOfFun(self,pm):
        x = []
        ymax = []
        ysum = []
        ynice = []
        yego = []
        yinit = []
        for p in pm.people:
            try:
                print("aggiungo "+str(p.id))
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
        plt.savefig("output/max_monthoffun.png")
        plt.close()

        plt.title('Summed year of fun')
        plt.ylabel('month of fun')
        plt.xlabel('people')
        plt.plot(x,ysum)
        plt.savefig("output/sum_monthoffun.png")
        plt.close()
