# Get input data
with open("input.txt") as f:
    input_data = f.read()

parts = input_data.split("\n\n")
# Stacks data
stack_lines = parts[0].split("\n")
stack_no = int(stack_lines[-1].split(" ")[-2])
stacks = [[] for i in range(stack_no)]
for line in stack_lines[:-1]:
    crates = line.replace("] [", "$").replace("]  ", "$").replace("  [", "$").replace("    ", "$").replace("[", "").replace("]", "").split("$")
    for i, c in enumerate(crates):
        if c.strip() != "":
            stacks[i].append(c)
# Moves data
moves_part = parts[1].split("\n")
moves = list(map(lambda x: x.replace("move ", "").replace(" from ", ",").replace(" to ", ",").split(","), moves_part))

# Moves on Stacks
s = stacks[:]
for move in moves:
    s[int(move[2])-1] = list(reversed(s[int(move[1])-1][:int(move[0])])) + s[int(move[2])-1]
    s[int(move[1])-1] = s[int(move[1])-1][int(move[0]):] if int(move[0]) < len(s[int(move[1])-1]) else []

res = "".join(list(map(lambda x: x[0], s)))
