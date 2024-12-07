with open("input.txt", "r") as file:
    data = file.read()

rows = data.strip().split("\n")

left_list = []
right_list = []

for row in rows:
    left_value, right_value = map(int, row.split())
    left_list.append(left_value)
    right_list.append(right_value)

left_list.sort()
right_list.sort()

# for l, r in zip(left_list, right_list):
#     difference = l - r
#     differences.append(difference)
difference = sum(abs(l - r) for l, r in zip(left_list, right_list))

print(difference)