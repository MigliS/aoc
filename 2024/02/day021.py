with open("input.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    # print("Line:", line)
    numbers = line.split()

    numbers = list(map(int, numbers))

    print("Numbers:", numbers)