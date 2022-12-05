from functools import reduce

with open("input.txt", "r") as f:
    input_data = f.read()

reduce(
    lambda count, r: count + (1 if (int(r[0]) <= int(r[2]) and int(r[1]) >= int(r[3])) or (int(r[0]) >= int(r[2]) and int(r[1]) <= int(r[3])) else 0),
    map(lambda p: p[0].split("-") + p[1].split("-"), map(lambda x: x.split(","), input_data.split("\n"))),
    0
)