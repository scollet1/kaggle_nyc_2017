# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    run.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: scollet <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/08/24 12:02:06 by scollet           #+#    #+#              #
#    Updated: 2017/08/24 12:02:07 by scollet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import csv
import datetime
import time
from copy import deepcopy
from tools import find_distance
from math import sin, cos, sqrt, atan2, radians

class Agent:
    def __init__(self):
        self.ID = 0
        self.duration = 0
        self.passengers = 0
        self.distance = 0
        self.vendor = 0
    def ID(self):
        return self._ID
    def duration(self):
        return self._duration
    def passengers(self):
        return self._passengers
    def distance(self):
        return self._distance
    def vendor(self):
        return self._vendor

with open('../train.csv', 'rb') as csvfile:
    agents = {}
    #agents[0][0] = {}
    next(csvfile)
    training_data = csv.reader(csvfile, delimiter=',')
    for row in training_data:
        agent = Agent
        agent.ID = row[0]
        agent.vendor = row[1]
        #agent.duration = convert_time(row[1], row[2]) #haha just kidding
        agent.passengers = row[4]
        agent.distance = find_distance(row[5], row[6], row[7], row[8])
        agent.duration = row[10]
        index = int(agent.distance)
        index2 = int(agent.duration)
        if not index in agents:
            agents[index] = {}
        if not index2 in agents[index]:
            agents[index][index2] = list()
        agents[index][index2].append(deepcopy(agent))
        #print agent.duration
        #agent = None
    for key, value in agents.items():
        for k, data in value.items():
            for i, point in enumerate(data):
                print i, point.duration
