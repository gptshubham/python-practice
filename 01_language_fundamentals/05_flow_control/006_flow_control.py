# conditional/ selection statements

# # Program -> write a program to find greatest of 3 given numbers
# a,b,c = 20,10,30
#
# if a>b>c:
#     print(a)
# elif b>c:
#     print(b)
# else:
#     print(c)

# Iterative Statements

# # Program -> print the sum of first n natural numbers
# n = 10
# sum_total = 0
# for i in range(10):
#     sum_total += (i+1)
#
# print(sum_total)

# Transfer Statements

# 1. break

# n = range(20)
# counter = 0
# for i in n:
#     counter += 1
#     if i==10:
#         print('found')
#         break
# print(counter)

# Qsn: Which Loop will break in case of following Programs:

# for i in range(10):
#     for j in range(10):
#         print(i,j)
#     if j == 5:
#         print('Loop Completed!')
#         break
# # none as the break condition is dependent on inner loop's j,
# # but it's been placed outside the scope of inner loop

# for i in range(10):
#     for j in range(10):
#         if i == 5:
#             print('Loop Skipped!')
#             break
#         print(i,j)

# 2. continue

for i in range(10):
    if i == 5:
        print('Loop Skipped!')
        continue
    print(f'order = {i}')

# print only odd numbers between 1 and 20
for i in range(20):
    if i%2 == 0:
        continue
    print(i)

# pass Statement
for i in range(10): pass

# # deleting an item of string object
# s = 'shubham'
# print(s[0])
# del s[0]
# # TypeError: 'str' object doesn't support item deletion