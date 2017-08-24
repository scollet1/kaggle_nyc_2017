/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   nyc.h                                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: scollet <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/08/20 02:16:46 by scollet           #+#    #+#             */
/*   Updated: 2017/08/20 02:16:47 by scollet          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef NYC_H
# define NYC_H
# include <stdlib.h>
# include <time.h>
# include <stdio.h>
# include <math.h>
# include <fcntl.h>
# include <unistd.h>
# include <string.h>
# include <ctype.h>

# define BUF_SIZE 4000
# define MAX_UID  4000000


typedef struct s_agent {
  struct s_ant  *next;
  struct s_ant  *previous;
  double        time;
  double        score;
}              t_agent;

typedef struct s_ride {
  struct s_ride   *next;
  struct s_ride   *previous;
  t_agent         *agent;
  double          distance;
}              t_ride;

#endif
