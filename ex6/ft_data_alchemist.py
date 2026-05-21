# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_data_alchemist.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mhashimo <mhashimo@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/21 21:10:27 by mhashimo          #+#    #+#              #
#    Updated: 2026/05/21 22:37:13 by mhashimo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

def main():
	print("=== Game Data Alchemist ===")
	print()
	name = ["Alice", "bob", "Charlie", "dylan", "Emma", "Gregory", "john", "kevin", "Liam"]
	print(f"Initial list of players: {name}")
	capitalized = [n.capitalize() for n in name]
	print(f"New list with all names capitalized: {capitalized}")
	capitals = [n for n in name if n[0].isupper()]
	print(f"New list of capitalized names only: {capitals}")
	print()
	score_dict = {n: random.randint(1, 1000) for n in capitalized}
	print(f"Score dict: {score_dict}")
	average = round(sum(score_dict.values()) / len(score_dict), 2)
	print(f"Score average is {average}")
	high_score = {key: value  for key, value in score_dict.items() if value > average}
	print(f"High scores: {high_score}")

if __name__  == "__main__":
	main()
