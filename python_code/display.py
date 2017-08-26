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

<<<<<<< HEAD
def display(agents, raw_data):
    agents = pandas.read_csv('../data_out.csv')
    agents.head()
    seaborn.lmplot(x="distance", y="time", data=agents, fit_reg=True).savefig('testing.png')
=======
def display():
	agents = pandas.read_csv('../data_out.csv')
	agents.head()
	seaborn.lmplot(x="distance", y="duration", data=agents, fit_reg=True).savefig('../test.png')

display()
>>>>>>> 5fa18a8c0697a45b550d7c1985449c487ae1f958
