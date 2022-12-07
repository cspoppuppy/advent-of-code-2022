from functools import reduce

with open("input.txt", "r") as f:
    input_data = f.read()

pairs = list(map(lambda p: p[0].split("-") + p[1].split("-"), map(lambda x: x.split(","), input_data.split("\n"))))
res1 = reduce(
    lambda count, r: count + (1 if (int(r[0]) <= int(r[2]) and int(r[1]) >= int(r[3])) or (int(r[0]) >= int(r[2]) and int(r[1]) <= int(r[3])) else 0),
    pairs, 0
)

res2 = reduce(
    lambda count, r: count + (1 if (int(r[0]) >= int(r[2]) and int(r[0]) <= int(r[3])) or (int(r[1]) >= int(r[2]) and int(r[1]) <= int(r[3])) \
        or (int(r[2]) >= int(r[0]) and int(r[2]) <= int(r[1])) or (int(r[3]) >= int(r[0]) and int(r[3]) <= int(r[1])) else 0),
    pairs, 0
)
