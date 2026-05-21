# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_data_stream.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mhashimo <mhashimo@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/19 21:17:34 by mhashimo          #+#    #+#              #
#    Updated: 2026/05/21 21:17:09 by mhashimo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

def gen_event():
	name = ["alice", "bob", "charlie", "dylan"]
	action = ["run", "eat", "sleep", "grab", "move", "climb", "release", "swim", "use"]
	while True:
		chosen_name = random.choice(name)
		chosen_action = random.choice(action)
		yield (chosen_name, chosen_action)

def consume_event(events_list):
	while events_list:
		chosen = random.choice(events_list)
		events_list.remove(chosen)
		yield chosen

def main():
	print("=== Game Data Stream Processor ===")
	event_gen = gen_event()
	for i in range(1000):
		tuple = next(event_gen)
		print(f"Event {i}: Player {tuple[0]} did action {tuple[1]}")
	events_list = []
	event_gen = gen_event()
	for i in range(10):
		events_list.append(next(event_gen))
	print(f"Built list of 10 events: {events_list}")
	for event in consume_event(events_list):
		print(f"Got event from list: {event}")
		print(f"Remains in list: {events_list}")

if __name__ == "__main__":
	main()
