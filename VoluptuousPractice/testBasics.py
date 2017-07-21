from voluptuous import Schema

class test:
    def __init__(self):
        print('testVoluptuous!!')
        my_schema = Schema({'name': str, 'email': str}, required=True, extra = True)
        my_schema({'name': '#topic', 'email': 'abc', 'testExtra':'ok'})

        getCards= Schema({'total_count': int,
                          'done_count':int,
                          'estimate_sum':int,
                          'overdue': any(list, dict)})
        getCards({'total_count':2,
                  'done_count':1,
                  'estimate_sum':23,
                  'overdue': {'key1':'value1'}})

        print('testSuccessful!!')



t = test()