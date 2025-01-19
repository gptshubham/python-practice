# strip(), rstrip(), lstrip() --> Removes spaces from the string
from traceback import print_tb

firstName = '             shubham            '
print(firstName)

firstName = firstName.strip()
print(firstName)

middleName = 'shubham           '
print(middleName)
print(len(middleName))

middleName = middleName.rstrip()
print(middleName)
print(len(middleName))

lastName = '         Gupta'
print(lastName)
lastName = lastName.lstrip()
print(lastName)

# finding the substring

# find(), rfind()
full_name = 'shubham kumar gupta'

index_position = full_name.find('kumar')
print(index_position)

index_position = full_name.find('z')
print(index_position)

index_position = full_name.find('a')
print(index_position)

index_position = full_name.find('a', 6, len(full_name))
print(index_position)

index_position = full_name.find('a', 12, len(full_name))
print(index_position)

index_position = full_name.rfind('a')
print(index_position)

# index()

index_position = full_name.index('a')
print(index_position)

# index_position = full_name.index('z')
# ValueError: substring not found

# replace()

full_name = full_name.replace('kumar', 'Kumar')
print(full_name)

full_name_list = full_name.split()
print(full_name_list)

full_name_join = ' '.join(full_name_list)
print(full_name_join)

# upper(), lower(), capitalize(), title(), swapcase()
print(full_name.upper())
print(full_name.lower())
print(full_name.capitalize())
print(full_name.title())
print(full_name.swapcase())

# isalpha(), isnumeric(), isdigit(), isalnum(), isspace(), islower(), isupper(), istitle()

firstName = 'Shubham'
print(firstName.isalpha())
uid = '1234'
print(uid.isnumeric())
print(uid.isdigit())
pan = 'ACBDE1234F'
print(pan.isalnum())

space = ' '
print(space.isspace())

print(firstName.islower())
print(firstName.isupper())
print(firstName.istitle())

# startswith(), endswith()
print(firstName.startswith('S'))
print(firstName.startswith('s'))

print(firstName.endswith('m'))
print(firstName.endswith('M'))

# Program 1 : write a program to reverse a given string
reversed_full_name = full_name[::-1]
print(reversed_full_name)

# alternatively: using reverse()
reversed_full_name_2 = reversed(full_name)
print(reversed_full_name_2)
print(type(reversed_full_name_2))
print(''.join(reversed_full_name_2))

# Program 2 : write a program to Reverse Order of Words in a string
full_name = 'Shubham Kumar Gupta'
full_name = ' '.join(full_name.split()[::-1])
print(full_name)

# Program 3 : write a program to reverse the internal content of each word
full_name = 'Shubham Kumar Gupta'
full_name = ' '.join([x[::-1] for x in full_name.split()])
print(full_name)

# Program 4 : Reverse Internal Content of every second word
words = 'one two three four five six seven eight nine ten'
words = words.split()
for position in range(len(words)):
    if position % 2 == 0:
        continue
    else:
        words[position] = words[position][::-1]
words = ' '.join(words)
print(words)

# Program 6: Merge characters of 2 strings into a single string by
# taking characters alternatively : salman, khan ==> skahlamnan
'''
first_word = input('Enter first word')
second_word = input('Enter second word')
output = ''
i=j=0
while i<len(first_word) or j<len(second_word):
    if i<len(first_word):
        output += first_word[i]
        i+=1
    if j<len(second_word):
        output += second_word[j]
        j+=1

print(output)
'''

# # Program 7:
# Input: ABCDEF and 123456
# Output: AA1BB2CC3DD4EE5FF6

letters = input('Enter letters: ').upper()
digits = input('Enter digits: ')

output = ''
for i in range(len(letters)):
    for j in range(len(digits)):
        if i==j:
            output += letters[i] * int(digits[j])
if len(letters) > len(digits):
    # handling the cases when length of letters is more than length of digits and
    # we get truncated output e.g; letters: abcde, digits: 123, output: ABBCCC
    output += letters[-(len(letters) - len(digits)):]

print(output)


