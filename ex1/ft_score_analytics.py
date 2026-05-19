# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_score_analytics.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mhashimo <mhashimo@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/18 22:38:47 by mhashimo          #+#    #+#              #
#    Updated: 2026/05/18 23:19:03 by mhashimo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main():
    print("=== Player Score Analytics ===")

    scores = []
    for s in sys.argv[1:]:
        try:
            scores.append(int(s))
        except ValueError:
            print(f"Invalid parameter: '{s}'")

    if len(scores) < 1:
        print(f"No scores provided. Usage: python3 {sys.argv[0]} <score1> <score2> ...")
        return

    print(f"Scores processed: {scores}")
    total = len(scores)
    print(f"Total players: {total}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / total}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")

if __name__ == "__main__":
    main()
