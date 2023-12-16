from itertools import combinations


list1 = [-1, 2, 1, 4]
target = 1
list2 = []

for i, j, k in combinations(list1, 3):
    list2.append(i+j+k-target)

# print(list2)
print(min(list2) + target)