# marriage-problem-simulation
An algorithm to simulate the marriage problem in a real world scenario where agent act not in an optimal way

#Introduction

After the reading of this italian article [http://leganerd.com/2016/11/11/il-problema-del-matrimonio-stabile/]("Il problema del matrimonio stabile") i decide to write
my own social implementation of this problem in a real world scenario.
Here the wikipedia article about the problem [https://en.wikipedia.org/wiki/Stable_marriage_problem](wikipedia.org)
I started setting up the problem as an agents based simulation, each agent is charaterised by two attribute:

- ego: the self confidence of a person, if you had a strong ego you do not accept a low quality marriage
- init: as initiative if you have a strong initiative you try to engage more partner and the stability of your marriage is weak

the simulation try to recreate a natural process of pairing and  selection, where people has embedded preference list of each partner.

#Usage

Edit the *main.py*
```
//simulationCore(number of people, year of simulation)
sm = SimulationCore(100,60)
```

run the simulation
```
python main.py
```
