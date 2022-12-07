with open("input.txt") as f:
    input_data = f.read()

calories_per_alf = list(map(lambda elf: sum(map(lambda x: int(x), elf.split("\n"))), input_data.split("\n\n")))
# part 1
res1 = max(calories_per_alf)

# part 2
res2 = sum(sorted(calories_per_alf, reverse=True)[:3])
