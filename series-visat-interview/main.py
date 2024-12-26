'''
# Input: Two numbers N and K
# N: 20
# K: 6
# Output: 20 14 8 2 -4 2 8 14 20

# N: 15
# K: 5
# 15 10 5 0 5 10 15 (15,5)
'''

N = int(input("N: "))
K = int(input("K: "))

flag = False # identify to perform which operation
temp = N
results = [temp] # list to store the results

# continue until the temp is reached to N and flag is True
while not (temp == N and flag == True):

    # for find the series from N to <= 0
    if temp > 0 and flag == False:
        temp -= K
        results.append(temp)
    # to find the series from <= 0 to N
    elif temp <= 0 and flag == False:
        flag = True
        temp += K
        results.append(temp)
    elif temp < N and flag == True:
        temp += K
        results.append(temp)

# printing the result
print(results)
