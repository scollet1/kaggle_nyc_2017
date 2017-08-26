# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    display.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: scollet <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/08/24 17:28:25 by scollet           #+#    #+#              #
#    Updated: 2017/08/24 17:28:27 by scollet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
import seaborn
import pandas as pandas

def display():
	agents = pandas.read_csv('../data_out.csv')
	#agents.head()
	seaborn.lmplot(x="distance", y="duration", data=agents, fit_reg=True).savefig('../test.png')

display()
