
class test_dictionary:
    def __init__(self):
        list_dict_values = {'ns1:Description':'My_desc', 'ns1:FatherKey':'12345'}
        list_of_dict = list_dict_values
        # print(list_dict_values)
        # print(list_of_dict)
        # for key in list_of_dict:
        # key1 = 'abc'
        # value1 = 'xyz'
        # list_of_dict.update({key1: value1})

        # for key in list_dict_values:
        #     value = list_dict_values[key]
        #     key = key.split(':')[1]
        #     print(key)
        #     print(value)

        list_of_dict = {key.replace('ns1:',''): list_dict_values[key] for key in list_dict_values.keys()}
        # for key in list_dict_values.keys():
        #     value = list_dict_values[key]
        #     key = key.replace('ns1:','')
        #     list_dict_values[key]=value

        print(list_dict_values)
        print("List of dict: ",list_of_dict)


if __name__ == '__main__':
    t = test_dictionary()