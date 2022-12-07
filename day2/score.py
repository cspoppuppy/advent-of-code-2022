from functools import reduce

with open("input.txt") as f:
    input_data = f.read()

oppo_map = {"A": 1, "B": 2, "C": 3}
player_map = {"X": 1, "Y": 2, "Z": 3}

res1 = reduce(
    lambda score, x: score + (3 if oppo_map.get(x[0], 0) == player_map.get(x[1], 0) else 0) + (6 if (player_map.get(x[1], 0) - oppo_map.get(x[0], 0))%3 == 1 else 0) + player_map.get(x[1], 0), 
    map(lambda x: x.split(" "), input_data.split("\n")), 0
)

player_res = {"X": 0, "Y": 3, "Z": 6}
score_map = {
    "A": {"X": 3, "Y": 1, "Z": 2},
    "B": {"X": 1, "Y": 2, "Z": 3},
    "C": {"X": 2, "Y": 3, "Z": 1}
}
res2 = reduce(
    lambda score, x: score + player_res[x[1]] + score_map[x[0]][x[1]], 
    map(lambda x: x.split(" "), input_data.split("\n")), 0
)