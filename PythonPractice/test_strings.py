str = 'Shalini'
print(str[3])
print("Lenght of String: ",len(str))
index = 0
while index< len(str):
    # print(str[index])
    index += 1

# for letter in str:
#     # print(letter)

for letter in str:
    print(letter)

    #Slicing:

print("Slicing Strings I: ", str[0:4])
print("Slicing II: ", str[:3])

#In operator

print('n' in str)

print("Type Function:", type(str))
print("Directory functions: ", dir(str))


# String Library
print("Find a string", str.find('ini'))

""" Replace, lower, upper, lstrip, rstrip, startswith """

# Parsing