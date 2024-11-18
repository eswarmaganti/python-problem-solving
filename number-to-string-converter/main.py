import traceback
from typing import List, Dict, Union

class Problem:

    def __init__(self)->None:
        self.config: Dict = {
            1:'one',
            2:'two',
            3:'three',
            4:'four',
            5:'five',
            6:'six',
            7:'seven',
            8:'eight',
            9:'nine',
            10:'ten',
            11:'eleven',
            12:'twelve',
            13:'thirteen',
            14:'fourteen',
            15:'fifteen',
            16:'sixteen',
            17:'seventeen',
            18:'eighteen',
            19:'nineteen',
            20:'tweenty',
            30:'thirty',
            40:'fourty',
            50:'fifty',
            60:'sixty',
            70:'seventy',
            80:'eighty',
            90:'ninety',
            100:'hundred',
            1000:'thousand',
            1000000:'million',
            1000000000:'billion'
        }
        self.places: List[int] = [1,10,100,1000,1000000,1000000000]
        self.result: List = []
    def convert_to_str(self, number: int):
        try:
            if 0 < number <= 19:
                return self.result.append(self.config.get(number))

            for place in sorted(self.places, reverse=True): # iterate over each place
                if number // place : #  if only the place is lessthan or equal to number
                    coef = number // place
                    if coef not in self.config.keys():
                        self.convert_to_str(number=coef)
                        self.number_text(number=place)
                    else:
                        self.number_text(number = coef, place = place)

                    # check if number is lessthan 19
                    rem = number % place
                    if 0 < rem <= 19:
                        return  self.number_text(number=rem)
                    else:
                        number = rem

        except Exception as e:
            traceback.print_exc()
            print(f'*** Error: Runtime Exception occured while converting the number to text: {str(e)} ***')

    def number_text(self,number: int, place: int=1):
        if place not in [10,1]: # if place is non zero convert both number and place
            self.result.append(self.config.get(number))
            self.result.append(self.config.get(place))
            return
        else: # if place is zero convert only the number
            # self.result[number*place] = self.config.get(number*place)
            self.result.append(self.config.get(number*place))
            return


if __name__ == "__main__":
    num = int(input("Enter a Number: "))
    obj = Problem()
    obj.convert_to_str(number=num)
    print(' '.join(obj.result))


'''
Test Case: 1
/usr/local/bin/python3.12 /Users/eswarmaganti/Developer/Projects/PycharmProjects/python-problem-solving/number-to-string-converter/main.py 
Enter a Number: 2000000
two million

Test Case: 2
/usr/local/bin/python3.12 /Users/eswarmaganti/Developer/Projects/PycharmProjects/python-problem-solving/number-to-string-converter/main.py 
Enter a Number: 999
nine hundred ninety nine

Test Case: 3
/usr/local/bin/python3.12 /Users/eswarmaganti/Developer/Projects/PycharmProjects/python-problem-solving/number-to-string-converter/main.py 
Enter a Number: 100123
hundred thousand one hundred tweenty three

Test Case: 4
/usr/local/bin/python3.12 /Users/eswarmaganti/Developer/Projects/PycharmProjects/python-problem-solving/number-to-string-converter/main.py 
Enter a Number: 999999
nine hundred ninety nine thousand nine hundred ninety nine

Test Case: 5
/usr/local/bin/python3.12 /Users/eswarmaganti/Developer/Projects/PycharmProjects/python-problem-solving/number-to-string-converter/main.py 
Enter a Number: 912900
nine hundred twelve thousand nine hundred

'''