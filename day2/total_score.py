from functools import reduce


with open("input.txt") as f:
    input_data = f.read()


oppo_map = {"A": 1, "B": 2, "C": 3}
player_map = {"X": 1, "Y": 2, "Z": 3}

tot_score = reduce(
    lambda score, x: score + (3 if oppo_map.get(x[0], 0) == player_map.get(x[1], 0) else 0) + (6 if (player_map.get(x[1], 0) - oppo_map.get(x[0], 0))%3 == 1 else 0) + player_map.get(x[1], 0), 
    map(lambda x: x.split(" "), input_data.split("\n")), 0
)
