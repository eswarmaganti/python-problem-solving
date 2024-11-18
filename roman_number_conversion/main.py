from typing import List, Dict

class Solution:
    def __init__(self, roman: str, decimal: int):
        self.roman = roman
        self.decimal = decimal

        self.roman_config: Dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        self.decimal_config: Dict = {
            1: 'I',
            4: 'IV',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

    def to_decimal(self) -> int:
        # reverse the roman numbers
        roman = self.roman[::-1]
        prev = roman[0]
        result = self.roman_config[prev]
        for r in roman[1:]:
            if self.roman_config[prev] <= self.roman_config[r]:
                result += self.roman_config[r]
            else:
                result -= self.roman_config[r]
            prev = r
        return result

    def to_roman(self):
        result = ''
        for place in [1000, 500, 100, 50, 10, 1]:
            if self.decimal // place != 0:
                right_dig = self.decimal // place
                result += right_dig * self.decimal_config[place]
                self.decimal = self.decimal % place
        else:
            return result


obj = Solution(roman='MMMDCL', decimal=650)
print(obj.to_decimal())
print(obj.to_roman())