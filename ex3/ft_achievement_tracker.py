# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_achievement_tracker.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mhashimo <mhashimo@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/19 17:11:17 by mhashimo          #+#    #+#              #
#    Updated: 2026/05/19 20:33:22 by mhashimo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

def gen_player_achievements():
	all_achievements = {'Crafting Genius', 'Strategist', 'World Savior',
 'Speed Runner', 'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
 'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind', 'Boss Slayer'}
	alice = set(random.sample(list(all_achievements), 4))
	bob = set(random.sample(list(all_achievements), 4))
	charlie = set(random.sample(list(all_achievements), 4))
	dylan = set(random.sample(list(all_achievements), 4))
	print(f"Player Alice: {alice}")
	print(f"Player Bob: {bob}")
	print(f"Player Charlie: {charlie}")
	print(f"Player Dylan: {dylan}")
	print()
	print(f"All distinct achievements: {all_achievements}")
	print()
	common_achievements = alice.intersection(bob, charlie, dylan)
	print(f"Common achievements: {common_achievements}")
	print()
	alice_difference = alice.difference(bob, charlie, dylan)
	bob_difference = bob.difference(alice, charlie, dylan)
	charlie_difference = charlie.difference(alice, bob, dylan)
	dylan_difference = dylan.difference(alice, bob, charlie)
	print(f"Only Alice has: {alice_difference}")
	print(f"Only Bob has: {bob_difference}")
	print(f"Only Charlie has: {charlie_difference}")
	print(f"Only Dylan has: {dylan_difference}")
	print()
	alice_missing = all_achievements.difference(alice)
	bob_missing = all_achievements.difference(bob)
	charlie_missing = all_achievements.difference(charlie)
	dylan_missing = all_achievements.difference(dylan)
	print(f"Alice is missing: {alice_missing}")
	print(f"Bob is missing: {bob_missing}")
	print(f"Charlie is missing: {charlie_missing}")
	print(f"Dylan is missing: {dylan_missing}")

def main():
	print("=== Achievement Tracker System ===")
	print()
	gen_player_achievements()

if __name__ == "__main__":
	main()
