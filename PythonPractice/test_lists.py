first_list= []
appendedList= []
second_list = []
extended_list = ['extended','list']
second_list.append("2ndList")
first_list.append("Shalini")
first_list.append(30)
first_list.append(43.66)
first_list.append('arora')
first_list.append('J')
#appendedList is list of lists()first_list and appendedList
appendedList.append(first_list)
appendedList.append(second_list)
print("First List:",first_list)
print("Second List:",second_list)
print("appendedList",appendedList)
print("extendedList:",extended_list.extend(second_list))

for item in first_list:
    print(item)
for item in appendedList:
    print(item)

print("Length:",len(first_list))

print("Sequence:", first_list[1:4:2])

for i in range(len(first_list)):
    print(i)

abc = 'sample'
print(abc+'.xml')

print("List:" , first_list[:4])
print("List:" , first_list[1:])