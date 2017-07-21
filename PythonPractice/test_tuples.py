t = ('1', 'abc','a','cde','34','dhdj')
print(t)
print(t[1])
print(t[5])

t = ('a','b','c','f','a','g','a')
print(t)

print(t.index('a'))
print(t.count('a'))



t1 = ((1,2,3)+(33,44,56,66),('a','b','c'))
print(t1)
print(3 in t1)
print(23 not in t1)

for item in t1:
    print("Item in tuple:", item)


tup1 = (True, False,True)
print("AND: ",all(tup1))  # if any 1 is FALSE
print("OR: ", any(tup1))   # if any one is True

print("Length of tuple: ", len(t))
print("Maximum in tuple", max(t))

print("Sum of tuple", sum(t1))
#Return an enumerate object. It contains the index and value of all the items of tuple as pairs.
print("Enumerate: ",enumerate(t))
del t


