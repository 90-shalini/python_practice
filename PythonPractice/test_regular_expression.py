import re

# To test regular expressiong in python

#  Test ^

line = "From : Shalini Arora"
if line.startswith('From'):
    print(line)

if re.search('^From', line):
    print(line)

# . wild card character
# . any character
# * any number of times
# + one or more times
# \S non whitespace character
# () start and stop extracting
# [ ] one character
test_line = 'Fromsss: Shalini , To Shalini'
if re.search('^From.*:', test_line):
    print(test_line)

numbers = 'My name is 1 and 2 and age is 23 , 34'
print(re.findall('[0-9]+', numbers))


sentence = 'From abc@gmail.com the messaise is OK'
print(re.findall('^From (\S+@\S+)', sentence))
print('Domain:', re.findall('@([^ ]*)', sentence))





