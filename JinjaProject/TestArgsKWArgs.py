from TestJinja import *

class testKWargs:
    def __init__(self):
        #case1:

        self.testfunc(isMilestone='true', enter_progress='true',schedule_start='2017-03-19T15:20:00')
        # self.testfunc(isMilestone='false', enter_progress='true', ActualStartDate = '2017-03-19T15:20:00')
        # self.testfunc(isMilestone='false', enter_progress='true')

    def testfunc(self, **kwargs):
        self.dict1 = {'key1':'value1', 'key2': 'value2'}
        update_desc = 'desc'
        fatherKey = 'Key/12345'
        self.list_of_values = {'Description': update_desc, 'key': fatherKey}
        self.list_of_values.update(**kwargs)
        print(self.list_of_values)

        test_obj = TestJinja()
        test_obj.newFileTemplate(self.list_of_values)

        # for key in kwargs:
        #     print("KWArgs arguements: ", (key, kwargs[key]))