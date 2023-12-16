from typing import List
from itertools import combinations


class CalculateClosestSum:
    def __init__(self, nums: List, target: int) -> None:
        self.nums = nums
        self.target = target

    def calculate_summation(self):
        self.summation = [sum(combination)
                          for combination in combinations(self.nums, 3)]

    def calculate_distances(self):
        self.distances = [(abs(self.target - s)) for s in self.summation]

    def find_closest_sum(self):
        self.calculate_summation()
        self.calculate_distances()
        min_index = self.distances.index(min(self.distances))
        return self.summation[min_index]


if __name__ == "__main__":
    cs1 = CalculateClosestSum(nums=[-1, 2, 1, -4], target=1)
    print(cs1.find_closest_sum())

    cs2 = CalculateClosestSum(nums=[0, 0, 0], target=1)
    print(cs2.find_closest_sum())
