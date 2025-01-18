import sys
"""
Resources:
- GeeksforGeeks: https://www.geeksforgeeks.org/python-sys-module/
"""

# # sys.stdin

# for line in sys.stdin:
#     if line.rstrip() == 'q':
#         break
#     print(f'input: {line}')
# print('Program ended...')

# sys.stdout

# for line in sys.stdin:
#     if line.rstrip() == 'q':
#         break
#     sys.stdout.write(f'You Entered: {line}')
# print('Program ended...')

# # sys.stderr

# def print_to_stderr(*a):
#     print(*a, file = sys.stderr)
#
# print_to_stderr('Hello World')

# # sys.argv

# # version of Python Interpreter with some additional information
# print(sys.version)
# # 3.11.11 (main, Dec  4 2024, 08:55:07) [GCC 11.4.0]

# # absolute path of the current file
# print(sys.argv[0])
# # list of arguments passed
# print(sys.argv[1:])
