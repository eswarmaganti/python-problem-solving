from typing import  List


class Solution:
    def __init__(self, data: List[int]):
        self.data = data

    def method1(self)-> List[int]:
        return list(dict.fromkeys(self.data))

    def method2(self) -> List[int]:
        result = []
        [result.append(item) for item in self.data if item not in result]
        return result


if __name__ == '__main__':
    obj = Solution(list(map(int, input().split(" "))))
    print(obj.method1())
    print(obj.method2())