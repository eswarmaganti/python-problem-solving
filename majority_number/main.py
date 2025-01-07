# Majority Number
# Input: [1,2,3,2,1,1]
# Output: 1

# method one using defaultdict

from collections import defaultdict
import operator

input_data = [1,1,2,2,2,1,1,3,3,5,5]

number_counts = defaultdict(int)
for item in input_data:
    number_counts[item] +=1

print(number_counts)

# method1 - using itemgetter
# majority_number = max(number_counts.items(), key=operator.itemgetter(1))[0]

# method 2 using lambda and dict key
#majority_number = max(number_counts, key=lambda key: number_counts[key])[0]

# method 3 using lambda with dict.items()
majority_number = max(number_counts.items(), key=lambda item: item[1] )[0]

print(f'majority number: {majority_number}')



# method two using plain iteration oly works with two numbers
input_data = [1, 1, 2, 2, 1, 2, 1]
candidate = None
count = 0
for item in input_data:
    if count == 0:
        candidate = item

    if candidate == item:
        count += 1
    else:
        count -= 1

print(f'majority_number: {candidate}')
