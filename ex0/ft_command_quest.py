# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_command_quest.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mhashimo <mhashimo@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/18 21:03:28 by mhashimo          #+#    #+#              #
#    Updated: 2026/05/18 21:57:42 by mhashimo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main():
	print("=== Command Quest ===")
	print(f"Program name: {sys.argv[0]}")
	total = len(sys.argv) - 1
	if total < 1:
		print("No arguments provided!")
	else:
		print(f"Arguments received: {total}")
	i = 1
	while i <= total:
		print(f"Argument {i}: {sys.argv[i]}")
		i += 1
	print(f"Total arguments: {total + 1}")

if __name__ == "__main__":
	main()
