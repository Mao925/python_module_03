# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_coordinate_system.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mhashimo <mhashimo@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/18 23:20:21 by mhashimo          #+#    #+#              #
#    Updated: 2026/05/19 17:02:35 by mhashimo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math

def get_player_pos(verbose) ->tuple :
	while True:
		user_input = input("Enter new coordinates as floats in format 'x,y,z': ")
		parts = [p.strip() for p in user_input.split(",")]
		if len(parts) != 3:
			print("Invalid syntax")
			continue
		try:
			values = []
			for p in parts:
				values.append(float(p))
		except ValueError as e:
			print(f"Error on parameter '{p}': {e}")
			continue
		my_tuple = tuple(values)
		break
	if verbose:
		print(f"Get a fisrt tuple: {my_tuple}")
		print(f"It includes: X={my_tuple[0]}, Y={my_tuple[1]}, Z={my_tuple[2]}")
		print(f"Distance to center: {round(math.sqrt(my_tuple[0] ** 2 + my_tuple[1] ** 2 + my_tuple[2] ** 2), 4)}")
	return my_tuple

def main():
	print("=== Game Coordinate System ===")
	print()
	print("Get a first set of coordinates")
	p1 = get_player_pos(verbose=True)
	print()
	print("Get a second set of coordinates")
	p2 = get_player_pos(verbose=False)
	dist = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)
	print(f"Distance between the 2 sets of coordinates: {round(dist, 4)}")

if __name__ == "__main__":
	main()
