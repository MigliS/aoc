from collections import Counter

with open("input.txt", "r") as file:
    data = file.read()

rows = data.strip().split("\n")

left_list = []
right_list = []

for row in rows:
    left_value, right_value = map(int, row.split())
    left_list.append(left_value)
    right_list.append(right_value)

right_count = Counter(right_list)
# print(right_count)

sim_score = 0
for num in left_list:
    count_right = right_count.get(num, 0)
    sim_score += num * count_right

print(sim_score)