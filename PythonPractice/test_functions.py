# There are two types of functions: the ones that you write yourself and include in your code,
# and the ones that are included in Python natively, which carry out common procedures,
# such as converting an integer to a string, or finding the length of a string. similar to user defined and predefined


# To define the function, we need to use the 'def' keyword,
# and then the name of the function. Next, we type two parentheses and then a colon

# should not return NONE from a function
def divide(a, b):
    try:
        return True, a/b
    except ZeroDivisionError:
        return False, None

status, value = divide(0, 0)
print('Status:', status)
print('output: ', value)

# testing normal function, local scope etc
cost1 = 12
cost2 = 45


def total_cost():
    return cost1+cost2


def final_cost(item1, item2):
    return item1+item2


# adding default arguments
def default_cost(data1, data2=4):
    return data1 + data2

abc = total_cost()
defg = final_cost(12, 22)
hij = default_cost(22)
print(abc, defg, hij)

number = 10
print('the number is ' + str(number))


# passing list of argument's
def avg(first, *rest):
    print("\nLength of args: ", len(rest))
    print('waste variable:')
    return (first + sum(rest))/(1+len(rest))

print(avg(1, 64, 66, 23, 21, 234, 5))
print("trying dictionary argument's:")


# '''passing dict of values as arguments'''
def full_names(**names):
    print("print kwargs:", names)
    for name in names:
        print("Name: ", names[name])

full_names(first='Shalini', last='Arora')


# return multiple values from a function
def multiple_returns(a, b):
    sum = a+b
    minus = a-b
    mul = a*b
    div = a/b
    return sum, minus, mul, div


x, y, z, p = multiple_returns(20, 10)
print(x, ':', y, ':', z, ':', p)
print(type(x))
print(type(multiple_returns(20, 10)))


# inline functions/ Anonymous functions == lambda
add = lambda x, y, z: x+y+z
print(add(1, 2, 3))
