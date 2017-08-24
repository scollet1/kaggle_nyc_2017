/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: scollet <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/08/20 02:31:08 by scollet           #+#    #+#             */
/*   Updated: 2017/08/20 02:31:09 by scollet          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "nyc.h"

t_ride  *file_init(t_ride *ride, char *arg)
{
  FILE          *fs;
  char          buffer[BUF_SIZE];
  char          *token;
  unsigned int  ID;
  double         x;
  double         y;
  double         dx;
  double         dy;
  double         distance;
  int           e_time;
  int           i;

  printf("begin read\n");
  ride->previous = NULL;
  ride->agent = (t_agent*)calloc(1000, sizeof(t_agent));
  ride->ride = 0.0;
  fs = fopen(arg, "r");
  printf("before line\n");
  while (fgets(buffer, sizeof(buffer), fs) != NULL)
  {
    i = -1;
    token = strtok(buffer, ",");
    token = strtok(NULL, ",");
    token = strtok(NULL, ",");
    token = strtok(NULL, ",");
    token = strtok(NULL, ",");
    token = strtok(NULL, ",");
    x = atof(token);
    token = strtok(NULL, ",");
    y = atof(token);
    token = strtok(NULL, ",");
    dx = atof(token);
    token = strtok(NULL, ",");
    dy = atof(token);
    distance = calculate_distance(x, y, dx, dy);
    while (++i < (int)distance)
    {
      if (ride->next == NULL) ride->next = new_ride(ride);
      ride = ride->next;
    }
    ride->distance = distance;
    token = strtok(NULL, ",");
    token = strtok(NULL, ",");
    ride->agent.time = atof(token);
    while (ride->previous) ride = ride->previous;
  }
  fclose(fs);
  return (ride);
}
