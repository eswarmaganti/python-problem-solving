# input: a list of elements
# output: print the odd one from the list

from typing import  List

def get_odd_one(input_data: List):
    input_data_map = {key:input_data.count(key) for key in set(input_data)}
    return {key:val for key,val in input_data_map.items() if val % 2 != 0}

    #print(input_data_map)

if __name__ == "__main__":
    print(get_odd_one([1,2,3,4,2,3,1,5,5]))