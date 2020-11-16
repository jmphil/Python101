# def funA()
#     return 0

# def funB()
#     return 0

# def multiple(a, b, c):

#     return a * a, b * b, c + c


# var1, var2, var3 = multiple(c=2, b=5, a=8)

# print(var1, var2, var3)

# import random
# import math

# def getAnswer(answerNumber):
#     if answerNumber == 1:
#         return 'It is certain'
#     elif answerNumber == 2:
#         return 'It is decidedly so'

# r = random.randint(1, 2)

# fortune = getAnswer(r)

# print(fortune)

# Write a function smallest that accepts a List of numbers as an argument.

# It should return the smallest number in the List.

import random


# def smallest(list):
#     min = list[ 0 ]
#     for a in list:
#         if a < min:
#             min = a
#     return min

# print(smallest([1 , 4, 6 , -10]))


# 2. Find the largest number
# Write a function largest that accepts a List of numbers as an argument.
# It should return the largest number in the List.



# def largest(list):
#     max = list[ 0 ]
#     for a in list:
#         if a > max:
#             max = a
#     return max

# print(largest([-10, 13, 100, -13]))

# 3. Find the shortest String
# Write a function shortest that accepts a List of Strings as an argument.

# It should return the shortest String in the List.


# def shortest(words_list):
#     word_len = []
#     for n in words_list:
#         word_len.append((len(n), n))
#     word_len.sort()
#     return word_len[-1][1]

# print (shortest(["hi", "lol", "goodbye", "greeting"])