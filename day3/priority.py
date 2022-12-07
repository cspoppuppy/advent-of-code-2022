from functools import reduce

with open("input.txt") as f:
    input_data = f.read()

lines = input_data.split("\n")

items = reduce(lambda r, s: r + list(set(s[:len(s)//2]) & set(s[len(s)//2:])), lines, [])
res1 = reduce(lambda r, i: r + (ord(i) - ord("a") + 1 if ord(i) >= ord("a") else ord(i) - ord("A") + 27), items, 0)

groups = [lines[i*3:(i+1)*3] for i in range(len(lines)//3)]
badges = list(map(lambda x: list(set(x[0]) & set(x[1]) & set(x[2]))[0], groups))
res2 = reduce(lambda r, i: r + (ord(i) - ord("a") + 1 if ord(i) >= ord("a") else ord(i) - ord("A") + 27), badges, 0)
