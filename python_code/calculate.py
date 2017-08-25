# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    engine.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: scollet <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/08/24 17:22:12 by scollet           #+#    #+#              #
#    Updated: 2017/08/24 17:22:13 by scollet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import tools
import random

def average(time):
    avrg = 0

    for duration, agents in time.items():
        if duration == "accuracy":
            pass
        else:
            for agent, data in enumerate(agents):
                #print data.ID
                avrg = data.duration + tools.find_neighbors(time, duration)
                avrg = int(avrg)
                avrg /= 3
                data.target = avrg

def accuracy(time):
    for duration, agents in time.items():
        sum_over = 1
        for members in range(len(agents) - 1):
            sum_over += 1
        for agent in agents:
            agent.accuracy += 1.000 / \
            ((float(agent.index) / sum_over) + 1)
            print agent.accuracy

def optimal(time):
    for duration, agents in time.items():
        for agent in agents:
            probability = agent.accuracy / tools.find_divisor(time, duration)
            if random.random <= probability:
                agent.remove(agent)
                if not duration in time.items():
                    time[agent.target] = {}
                time[agent.target].append(agent)
