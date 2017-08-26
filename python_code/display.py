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

import seaborn

def display(agents, raw_data):
    seaborn.lmplot(x="distance", y="time", data=agents)
