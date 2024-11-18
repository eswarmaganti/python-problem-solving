

class Solution:
    def __init__(self, number: int):
        self.number: int = number

    def is_perfect_prime(self):
        start, end = 1, self.number

        while start <= end:
            pivot = (start + end) // 2
            pivot_square = pivot ** 2

            if self.number == pivot_square:
                return True
            elif self.number < pivot_square:
                end = pivot - 1
            else:
                start = pivot + 1
        else:
            return False

    def is_perfect_prime_recursive(self, number: int, start: int, end: int):
        
        pivot = (start + end) // 2
        pivot_square = pivot ** 2
        if start > end:
            return False

        if number == pivot_square:
            return True
        elif number < pivot_square:
            return self.is_perfect_prime_recursive(number, start=start, end=pivot-1)
        else:
            return self.is_perfect_prime_recursive(number, start=pivot + 1, end=end)


number = int(input("Enter a Number: "))
obj = Solution(number)
print(obj.is_perfect_prime())
print(obj.is_perfect_prime_recursive(number, start=1, end=number))
