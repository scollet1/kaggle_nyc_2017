/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: scollet <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/08/20 02:06:58 by scollet           #+#    #+#             */
/*   Updated: 2017/08/20 02:06:59 by scollet          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "nyc.h"

void  error(err)
{
  exit(err);
}

int   main(int ac, char **av)
{
  t_distance  *distance;
  time_t        t;
  int           max_uid;

  /*
  ** TODO :
  **  - init distance
  **  - init paths
  **  - calculate each time tick
  **  - hopefully converge
  */

  t = 0;
  max_uid = 0;
  srand((unsigned)time(&t));
  distance = (t_distance*)calloc(1, sizeof(t_distance));
  if (!strcmp("random", av[1])) {distance = random_init(distance); max_uid = 150;}
  else if (!strcmp("file", av[1])) {distance = file_init(distance, av[2]);}
  printf("Starting simulation... !\n");
  run(distance);
  if (distance)
    free(distance);
  return (0);
}
