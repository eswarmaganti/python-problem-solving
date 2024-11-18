class Solution:
    def __init__(self, number: int):
        self.number = number

    def factorial(self, number: int) -> int:
        if number in [0,1]:
            return 1
        else:
            return number * self.factorial(number-1)

    def find_trailing_zeros(self) -> int:
        fact = self.factorial(self.number)
        print(f'fact({self.number}) = {fact}')

        # finding the trailing zero count
        zeros_count: int = 0
        while fact % 10 == 0:
                zeros_count += 1
                fact //= 10
        else:
            return zeros_count


if __name__ == "__main__":
    obj = Solution(int(input("Enter a Number: ")))
    print(obj.find_trailing_zeros())