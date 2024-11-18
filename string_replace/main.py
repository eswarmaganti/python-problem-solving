from typing import List


class Solution:
    def __init__(self, inp_str: str):
        self.inp_str = inp_str

    def replace_str_char(self, ch: str = ' ', replace_ch='') -> str:
        items: List[str] = list(self.inp_str)
        items = [item if item != ch else replace_ch for item in items]
        return ''.join(items)


if __name__ == "__main__":
    obj = Solution(input())
    print(obj.replace_str_char())