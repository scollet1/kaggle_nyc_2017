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

def find_divisor(neighbor, time):
    n = 0
    m = 0

    if time + 1 in neighbor:
        n = random.choice(neighbor[time + 1]).accuracy
    else:
        n = random.choice(neighbor[time]).accuracy
    if time - 1 in neighbor:
        m = random.choice(neighbor[time - 1]).accuracy
    else:
        m = random.choice(neighbor[time]).accuracy
    return n + m

def find_neighbors(neighbor, time):
    n = 0
    m = 0

    #print "TIME IN NEIGHBORS : ", time
    if time + 1 in neighbor:
        n = random.choice(neighbor[time + 1]).duration
    else:
        n = random.choice(neighbor[time]).duration
    if time - 1 in neighbor:
        m = random.choice(neighbor[time - 1]).duration
    else:
        m = random.choice(neighbor[time]).duration
    #print "N AND M : ", n, m
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
