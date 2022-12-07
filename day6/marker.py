with open("input.txt", "r") as f:
    input_data = f.read()

for i in range(len(input_data)):
    marker = input_data[i: i+4]
    if len(set(marker)) == 4:
        res1 = i + 4
        break


for i in range(len(input_data)):
    marker = input_data[i: i+14]
    if len(set(marker)) == 14:
        res2 = i + 14
        break
