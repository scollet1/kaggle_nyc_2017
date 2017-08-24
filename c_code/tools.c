/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tools.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: scollet <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/08/20 02:33:25 by scollet           #+#    #+#             */
/*   Updated: 2017/08/20 02:33:27 by scollet          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "nyc.h"

t_ride  new_ride(t_ride ride)
{
  t_ride  *new;

  new = (t_ride*)calloc(1, sizeof(t_ride));
  new->next = NULL;
  new->previous = ride;
  new->agent = (t_agent*)calloc(1, sizeof(t_agent));
  return (ride);
}

double  radian(double degree)
{
  double  radian;

  radian = degree * (M_PI / 180)
  return (radian);
}

double  calculate_distance(double x, double y, double dx, double dy)
{
  double  distance;
  double  radius;
  double  delta_lat;
  double  delta_lon;
  double  a;
  double  c;

  distance = 0.0;
  radius = 6371;

  x = radian(x);
  y = radian(y);
  dx = radian(dx);
  dy = radian(dy);
  delta_lat = dx - x;
  delta_lon = dy - y;
  a = sin(delta_lat / 2) * sin(delta_lat / 2) +
      cos(x) * cos(y) * sin(delta_lon / 2) *
      sin(delta_lon / 2);
  c = 2 * atan2(sqrt(a), sqrt(1 - a));
  distance = radius * c;
  return (distance);
}
