with open("input.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    # print("Line:", line)
    # numbers = line.split()

    # numbers = list(map(int, numbers))
    numbers = list(map(int, line.split()))

    differences = [numbers[i+1] - numbers[i] for i in range(len(numbers) - 1)]

    # print("Numbers:", numbers)
    print("Differences:", differences)