from functools import reduce

with open("input.txt") as f:
    input_data = f.read()

items = reduce(lambda r, s: r + list(set(s[:len(s)//2]) & set(s[len(s)//2:])), input_data.split("\n"), [])
priority = reduce(lambda r, i: r + (ord(i) - ord("a") + 1 if ord(i) >= ord("a") else ord(i) - ord("A") + 27), items, 0)
