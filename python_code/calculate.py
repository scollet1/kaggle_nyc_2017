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

def average(time):
    avrg = 0

    for dur, agents in time.items():
        #print "DUR : ", dur
        for data in agents:
            #print "DISTANCE, DURATION : ", data.distance, data.duration
            avrg = data.index2 + tools.find_neighbors(time, dur)
            #print "AVERAGE : ", avrg
            avrg /= 3
            #print "AVERAGE AFTER DIVIDE : ", avrg
            avrg = int(avrg)
            data.target = avrg

def accuracy(time):
    for duration, agents in time.items():
        sum_over = 1
        for members in range(len(agents)):
            sum_over += 1
            #print members
        for agent in agents:
            agent.accuracy += 1.000 / \
            ((float(agent.index) / sum_over) + 1)
            #print "AGENT ACCURACY : ", agent.accuracy

def optimal(time):
    for duration, agents in time.items():
        print duration
        for agent, data in enumerate(agents):
            #print agent
            probability = data.accuracy / tools.find_divisor(time, duration)
            #print "PROBABILITY OF SWITCHING : ", probability
            if random.random() <= probability:
                agents.remove(data)
                if not data.target in time.items():
                    time[data.target] = []
                time[data.target].append(data)
                data.index2 = data.target
