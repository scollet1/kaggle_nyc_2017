# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tools.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: scollet <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/08/24 13:05:31 by scollet           #+#    #+#              #
#    Updated: 2017/08/24 13:05:32 by scollet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from math import sin, cos, sqrt, atan2, radians
import random
import sys

def debug(agent):
    print agent.ID
    print agent.duration
    print agent.index2
    print agent.distance
    print agent.index
    print agent.accuracy
    print "AGENT TARGET : ", agent.target

def find_divisor(neighbor, duration):
    #print neighbor.keys()
    #print duration + 1
    if duration + 1 in neighbor:
        n = random.choice(neighbor[duration + 1]).accuracy
    elif duration in neighbor:
        n = random.choice(neighbor[duration]).accuracy
    else:
        n = 1
    if duration - 1 in neighbor:
        b = random.choice(neighbor[duration - 1])
        if type(b) is int:
            return 1
        print b
        debug(b)
        print b.accuracy
        m = b.accuracy
    elif duration in neighbor:
        m = random.choice(neighbor[duration]).accuracy
    else:
        m = 1
    return n + m

def find_neighbors(neighbor, duration):
    n = 0
    m = 0

    #print "duration IN NEIGHBORS : ", duration
    if duration + 1 in neighbor:
        n = random.choice(neighbor[duration + 1]).index2
    else:
        n = random.choice(neighbor[duration]).index2
    if duration - 1 in neighbor:
        m = random.choice(neighbor[duration - 1]).index2
    else:
        m = random.choice(neighbor[duration]).index2
    print "N AND M : ", n, m
    return n + m

'''
def set_field(agents, field="None"):
    if field == "None":
        pass
    else:
        for distance, duration in agents.items():
            for time, data in duration.items():
                if field == "accuracy":
    return agents
'''

def find_distance(lon, lat, dlong, dlat):
    distance = 0
    radius = 6371
    delta_lat = 0
    delta_lon = 0
    x = 0
    y = 0
    dx = 0
    dy = 0
    a = 0
    c = 0

    x = radians(float(lon))
    y = radians(float(lat))
    dx = radians(float(dlong))
    dy = radians(float(dlat))
    delta_long = dx - x
    delta_lat = dy - y
    a = sin(delta_lat / 2) * sin(delta_lat / 2) + \
        cos(x) * cos(y) * sin(delta_lon / 2) * \
        sin(delta_lon / 2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = radius * c
    return distance

def convert_time(start_date, end_date):
    time = 0
    start = 0
    end = 0

    start_date = start_date.split()
    end_date = end_date.split()
    start = time.strptime(start_date[1].split(",")[0],"%H:%M:%S")
    end = time.strptime(end_date[1].split(",")[0],"%H:%M:%S")
    start = datetime.timedelta(
            hours=start.tm_hour,
            minutes=start.tm_min,
            seconds=start.tm_sec).total_seconds()
    end = datetime.timedelta(
          hours=end.tm_hour,
          minutes=end.tm_min,
          seconds=end.tm_sec).total_seconds()
    time = abs(start - end)
    return time
