# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    run.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: scollet <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/08/24 12:02:06 by scollet           #+#    #+#              #
#    Updated: 2017/08/28 22:46:49 by scollet          ###   ########.fr        #
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

EPOCHS = 100

class Agent:
    def __init__(self):
        self.ID = 0
        self.duration = 1
        self.target = 0
        self.passengers = 0
        self.distance = 0
        self.vendor = 0
        self.accuracy = 0
        self.index = 0
        self.index2 = 0
    def ID(self):
        return self._ID
    def duration(self):
        return self._duration
    def target(self):
        return self._target
    def passengers(self):
        return self._passengers
    def distance(self):
        return self._distance
    def index(self):
        return self._index
    def index2(self):
        return self._index2
    def vendor(self):
        return self._vendor
    def accuracy(self):
        return self._accuracy


def parse(agents):
    with open('../train.csv', 'rb') as csvfile:
        next(csvfile)
        training_data = csv.reader(csvfile, delimiter=',')
        for row in training_data:
            agent = Agent()
            agent.ID = row[0]
            agent.vendor = row[1]
            agent.passengers = int(row[4])
            agent.distance = float(tools.find_distance(row[5], row[6], row[7], row[8]))
            index = int(agent.distance) + 1
            if int(row[10]) > 15000:
                continue
            if index > 100.0:
                continue
            agent.duration = int(row[10])
            agent.index = index
            index2 = agent.duration
            agent.index2 = index2
            #print "INDICES : ", index, index2
            if not index in agents:
                agents[index] = {}
            if not index2 in agents[index]:
                agents[index][index2] = []
            agents[index][index2].append(deepcopy(agent))
            #for key, value in agents.items():
            #    for k, data in value.items():
            #        for i, point in enumerate(data):
            #            print i, point.duration, point.ID, point.vendor
        return agents

def write_data(agents):
	with open('../data_out.csv', 'wb') as csvfile:
		writer = csv.writer(csvfile, delimiter=',')
		writer.writerow(['distance', 'duration'])
		for distance, time in agents.items():
			for dur, agents in time.items():
				for agent, data in enumerate(agents):
					writer.writerow([data.index, data.index2])
					#print "LENGTH AND TIME : ", data.index, data.duration

def run():
    random.seed()
    agents = {}
    parse(agents)
    #agents = tools.set_field(agents, "accuracy") # NOTE : maybe come back to this
    #agents = tools.set_field(agents, "max_distance") # NOTE : come back to this
    #agents = tools.set_field(agents, "max_duration") # NOTE : come back to this
    print "before copy data"
    #raw_data = deepcopy(agents)
    for i in range(EPOCHS):
        for length, time in agents.items():
            calculate.average(time)
            #sys.exit(0)
            print "leave avg"
            calculate.accuracy(time)
            print "leave acc"
            calculate.optimal(time)
            print "leave opt"
            #sys.stdout.flush()
            print length
        print "Epoch : ", i
        #sys.stdout.flush()
    #calculate.ground_truth(raw_data) # TODO : FINISH WRITING
    #sys.exit(0)
    write_data(agents)
    #display()

run()
