##v1

# numbers = [1, 5, 6, 8, 9]
#
# numbers.insert(0, numbers[-1])
# numbers.pop()
# print(numbers)

#v2

numbers = [1, 3, 25, 7, 2, 7]

numbers_p = [numbers[-1]]
numbers_min = numbers[0:-1]
result = numbers_p + numbers_min

print(result)