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
    start = time.strptime(start_date[1].split(',')[0],'%H:%M:%S')
    end = time.strptime(end_date[1].split(',')[0],'%H:%M:%S')
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
