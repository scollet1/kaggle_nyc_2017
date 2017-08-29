# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    display.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: scollet <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/08/24 17:28:25 by scollet           #+#    #+#              #
#    Updated: 2017/08/28 23:01:40 by scollet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
import seaborn
import pandas as pandas

def display():
	agents = pandas.read_csv('../data_out.csv')
	seaborn.set()
	seaborn.set_context("paper")
	#agents.head()
	seaborn.lmplot(x="distance", y="duration", \
	data=agents, size=4, aspect=2, fit_reg=True,).savefig('../test.png')

display()
