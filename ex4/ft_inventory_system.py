# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_inventory_system.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mhashimo <mhashimo@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/19 20:35:26 by mhashimo          #+#    #+#              #
#    Updated: 2026/05/19 21:16:32 by mhashimo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main():
	print("=== Inventory System Analysis ===")
	inventory = {}
	for arg in sys.argv[1:]:
		parts = arg.split(':')
		if len(parts) != 2:
			print("Error - invalid parameter '" + arg + "'")
			continue
		key = parts[0]
		value_str = parts[1]
		try:
			value = int(value_str)
		except ValueError as e:
			print("Quantity error for '" + key + "': " + str(e))
			continue
		if key in inventory.keys():
			print("Redundant item '" + key + "' - discarding")
			continue
		inventory.update({key: value})
	print("Got inventory: ", inventory)
	keys = list(inventory.keys())
	value_sum = sum(inventory.values())
	print(f"Item list: {keys}")
	print(f"Total quantity of the {len(keys)} items : {value_sum}")
	for key in keys:
		print(f"Item {key} represents {round(inventory[key] / value_sum * 100, 1)}%")
	max_key = max(inventory, key=inventory.get)
	min_key = min(inventory, key=inventory.get)
	print(f"Item most abundant: {max_key} with quantity {max(inventory.values())}")
	print(f"Item least abundant: {min_key} with quantity {min(inventory.values())}")
	inventory.update({'magic_item' : 1})
	print(f"Updated inventory: {inventory}")

if __name__ == "__main__":
	main()
