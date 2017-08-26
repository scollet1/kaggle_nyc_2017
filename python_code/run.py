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
import tools
import calculate
import sys
#from display import display # NOTE : thing go here
import random
from copy import deepcopy
from math import sin, cos, sqrt, atan2, radians

EPOCHS = 5

class Agent:
    def __init__(self):
        self.ID = 0
        self.duration = 0
        self.target = 0
        self.passengers = 0
        self.distance = 0
        self.vendor = 0
        self.accuracy = 0
        self.index = 0
    def ID(self):
        return self._ID
    def duration(self):
        return self._duration
    def target(self):
        return self._duration
    def passengers(self):
        return self._passengers
    def distance(self):
        return self._distance
    def index(self):
        return self._index
    def vendor(self):
        return self._vendor
    def accuracy(self):
        return self._accuracy


def parse():
    with open('../train.csv', 'rb') as csvfile:
        agents = {}
        #agents[0][0] = {}
        next(csvfile)
        training_data = csv.reader(csvfile, delimiter=',')
        for row in training_data:
            agent = Agent()
            agent.ID = row[0]
            agent.vendor = row[1]
            agent.passengers = int(row[4])
            agent.distance = float(tools.find_distance(row[5], row[6], row[7], row[8]))
            agent.duration = int(row[10])
            index = int(agent.distance)
            agent.index = index
            index2 = int(agent.duration)
            if not index in agents:
                agents[index] = {}
            if not index2 in agents[index]:
                agents[index][index2] = list()
            agents[index][index2].append(deepcopy(agent))
            #for key, value in agents.items():
            #    for k, data in value.items():
            #        for i, point in enumerate(data):
            #            print i, point.duration, point.ID, point.vendor
    return agents

def write_data(agents, raw_data):
    with open('../data_out.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['distance', 'duration'])
        for distance, time in agents.items():
            for duration, agent in time.items():
                print distance, duration
                writer.writerow([distance, duration])

def run():
    random.seed()
    agents = parse()
    #agents = tools.set_field(agents, "accuracy") # NOTE : maybe come back to this
    #agents = tools.set_field(agents, "max_distance") # NOTE : come back to this
    #agents = tools.set_field(agents, "max_duration") # NOTE : come back to this
    raw_data = agents
    for i in range(EPOCHS):
        for distance, time in agents.items():
            calculate.average(time)
            #print "leave avg"
            calculate.accuracy(time)
            #print "leave acc"
            calculate.optimal(time)
            print distance
            sys.stdout.flush()
            #print "leave opt"
        print "Epoch : ", i
        sys.stdout.flush()
    #calculate.ground_truth(raw_data) # TODO : FINISH WRITING
    #sys.exit(0)
    write_data(agents, raw_data)
    #display()

run()
