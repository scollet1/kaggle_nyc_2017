# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    calculate.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: scollet <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/08/24 17:22:12 by scollet           #+#    #+#              #
#    Updated: 2017/08/27 05:29:20 by scollet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import tools
import random
import sys

def average(time):
    avrg = 0
    for dur, agents in time.items():
        #print "DUR : ", dur
        for a in range(len(agents)):
            #print "DISTANCE, DURATION : ", data.distance, data.duration
            avrg = agents[a].index2 + tools.find_neighbors(time, agents[a].index2)
            #print "AVERAGE : ", avrg
            avrg /= 3
            #print "AVERAGE AFTER DIVIDE : ", avrg
            avrg = int(avrg)
            agents[a].target = avrg

def accuracy(time):
    for duration, agents in time.items():
        sum_over = 1
        for members in range(len(agents)):
            sum_over += 1
            #print members
        for a in range(len(agents)):
            dist = abs(float(agents[a].index2) - float(agents[a].target))
            if dist == 0:
                dist = 1
            step = 1.000 / dist
            #print "AGENT ACCURACY : ", step
            agents[a].accuracy += step

def optimal(time):
    for dur, agents in time.items():
        #print dur
        #print agents
        #sys.exit(0)
        #for a in range(len(agents)):
            #print agents[a].accuracy
        #sys.exit(1)
        for i, a in enumerate(agents):
            #print agents[a].accuracy
            #print a
            probability = a.accuracy / tools.find_divisor(time, a.index2)
            #print "PROBABILITY OF SWITCHING : ", probability
            if random.random() <= probability:
                #print "SWITCHED!!"
                if not a.target in time:
                    time[a.target] = []
                time[a.target].append(a)
                if not a in time[a.index2]:
                    pass
                else:
                    time[a.index2].remove(a)
                if not time[a.index2]:
                    del time[a.index2]
                a.index2 = a.target
                #print time[agents[a].index2]
            else:
                pass
