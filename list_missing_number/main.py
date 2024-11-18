from typing import List

class Solution:
    def __init__(self,num: int, data: List[int]):
        self.data = data
        self.num = num

    def find_missing_number(self):
        sum_of_list = sum(self.data)
        sum_of_num = self.num * (self.num + 1) // 2
        return sum_of_num - sum_of_list


if __name__ == "__main__":
    obj = Solution(8, [1, 3, 2, 5, 4, 8, 6])
    print(obj.find_missing_number())

