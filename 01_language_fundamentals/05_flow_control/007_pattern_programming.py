# # 1. print the given number of stars
#
# n = int(input('Enter number of stars: '))
# for i in range(n):
#     print('* ', end='')
#
# print()
#
# # alternatively, using string repetition
# print('* ' * n)
from tokenize import endpats

# # 2A. square patterns
#
# n = int(input('enter the number of rows: '))
#
# for i in range(n):
#     for j in range(n):
#         print('* ', end='')
#     print()
#
# print()
#
# # alternatively: using string repetition
# for i in range(n):
#     print('* ' * n)

# # 2B. Square Pattern: R1->A,R2->B,R3->C,.....
#
# n = int(input('Enter the number of rows: '))
#
# ordinate = ord('A')
#
# for i in range(n):
#     for j in range(n):
#         print(f'{chr(ordinate)} ',end='')
#     print()
#     ordinate += 1

# # 2C. Square Pattern: 1 2 3 4 5 * n times Row-wise
#
# n = int(input('Enter the number of rows: '))
#
# for i in range(n):
#     for j in range(n):
#         print(f'{j+1} ', end='')
#     print()

# # 3A. Right Angle Triangle: * Pattern
#
# n = int(input('Enter the number of rows: '))
#
# for i in range(n):
#     for j in range(i + 1):
#         print('* ', end='')
#     print()

# # 3B. Right Angle Triangle: number pattern 1,22,333,4444,55555
#
# n = int(input('Enter the number of rows: '))
#
# for i in range(n):
#     for j in range(i+1):
#         print(f'{i+1} ', end='')
#     print()

# # 3C. Right Angle Triangle: number pattern 1,12,123,1234,12345
#
# n = int(input('Enter the number of rows: '))
#
# for i in range(n):
#     for j in range(i+1):
#         print(f'{j+1} ', end='')
#     print()

# # 3D. Right Angle Triangle: number pattern 5,54,543,5432,54321
#
# n = int(input('Enter the number of rows: '))
#
# for i in range(n, 0, -1):
#     for j in range(n+1 - i):
#         print(f'{n-j} ', end='')
#     print()

# # 3E. Right Angle Triangle: number pattern
# # 1,21,321,4321,54321
#
# n = int(input('Enter the number of rows: '))
# for i in range(n, 0, -1):
#     for j in range(n+1 - i, 0, -1):
#         print(f'{j} ', end='')
#     print()

# # 4. Pyramid * Pattern
# n = int(input('Enter the number of rows: '))
# for i in range(n):
#     for j in range(n-1, -1, -1):
#         if i >= j:
#             print('* ', end='')
#         else:
#             print(' ', end='')
#     print()
#
# print()
# # Note: it worked here in case of pyramid pattern, but we can't use it's extended
# # version in case of dimond pattern, however, we can use the extended version of
# # the alternate approach in case of dimond pattern

# # alternatively: (what we have been taught)
# for i in range (n):
#     print(' '*(n-i-1),end='')
#     print('* '*(i+1))


# 5. Hollow Diamond --> those two stars at both ends