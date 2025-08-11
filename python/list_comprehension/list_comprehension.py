# List comprehension - A concise way to create lists in python.
#                      Compact and easier to read than traditional loops
#                      ['expression' for 'value' in 'iterable' 'condition']


nums = [1,-3,5,-8,-4,7,-2,14]

positive_nums = [num for num in nums if num >= 0]
print(f'Positive numbers: {positive_nums}')

negative_nums = [num for num in nums if num < 0]
print(f'Negative numbers: {negative_nums}')

even_nums = [num for num in nums if num % 2 == 0]
print(f'Even numbers: {even_nums}')

odd_nums = [num for num in nums if num % 2 == 1]
print(f'Even numbers: {odd_nums}')


grades = [85, 42, 78, 30, 81]

passing_grades = [grade for grade in grades if grade >= 60]
print(f'Passing grades: {passing_grades}')