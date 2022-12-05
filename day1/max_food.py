with open("input.txt") as f:
    input_data = f.read()

max(map(lambda elf: sum(map(lambda x: int(x), elf.split("\n"))), input_data.split("\n\n")))
