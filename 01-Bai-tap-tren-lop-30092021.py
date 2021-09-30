

# 1. Write a Python program to sum all the items in a list. (sum() function)
numbers = [1, 2, 3, 4, 5, 1, 4, 5]
Sum = sum(numbers)
print(f'Sum all the items in a list {Sum}')
# 2. Write a Python program to multiply all the items in a list. (math.prod() function)
# Importing math module
import math
# list
arr = [1, 2, 3, 4, 5]
product = math.prod(arr)
print(f'Multiply all the items from arr = [1, 2, 3, 4, 5]:. {product}')
# 3. Write a Python program to get the largest number from a list. (max() function)
print(f'The largest number from arr = [1, 2, 3, 4, 5]: {max(arr)}')
# 4. Write a Python program to get the smallest number from a list. (min() function)
print(f'The smallest number from arr = [1, 2, 3, 4, 5]: {min(arr)}')
# 5. Write a Python program to sort a list in descending order (sort() function)
numbers1 = [1, 3, 4, 2]
# Sorting list of Integers in descending
numbers1.sort(reverse=True)
print(f'Sorting numbers1 of Integers in descending: {numbers1}')
# 6. Write a Python program to sort a list in ascending order (sort() function)
numbers2 = [1, 3, 4, 2]
# Sorting list of Integers in ascending
numbers2.sort()
print(f'Sorting numbers2 of Integers in ascending: {numbers2}')
# 7. Write a Python program to get the size of a list (len() function)
print(f'Get the size of a numbers2: {len(numbers2)}')
# 8. Write a Python program to get random element(s) of a list (random.choice() function)
import random
number_list = [111, 222, 333, 444, 555]
# random item from list
print(f'Get random element(s) of a number_list: {random.choice(number_list)}')
# Output 222
# 9. Write a Python program to join two different lists into one (use + or extend() function)
# Initializing lists
test_list3 = [1, 4, 5, 6, 5]
test_list4 = [3, 5, 7, 2, "Love VietNam"]

# using list.extend() to concat
test_list3.extend(test_list4)

# Printing concatenated list
print("Concatenated list using list.extend() : "
      + str(test_list3))