with open("input.txt", "r") as file:
    data = file.read()

rows = data.strip().split("\n")

left_list = []
right_list = []

for row in rows:
    left_value, right_value = map(int, row.split())
    left_list.append(left_value)
    right_list.append(right_value)

# ll = min(left_list)
# lr = min(right_list)
left_list.sort()
right_list.sort()

differences = []

for l, r in zip(left_list, right_list):
    difference = l - r
    differences.append(difference)


print(sum(differences))
