from cerberus import Validator

class cerberusTest:
    def __init__(self):
        print("Test Cerberus!!")

        #Basic test
        schema = {'name':{'type':'string'}}
        v = Validator(schema)
        response = {'name':'Shalini Arora'}
        print("Basic Test: ", v.validate(response))


        #Adding more constraints to a field
        schema = {'name': {'type': 'string', 'maxlength': 10}}
        print("\nValidating values: ", v.validate({'name': 'ShaliniArora12344'}, schema))
        print(v.errors)

        #Testing extras
        print("\nTesting Extras: ", v.validate({'name': 'Shalini', 'age':30}), schema)
        print(v.errors)

        # Testing extras + error
        print("\nTesting value errors and extras: ", v.validate({'name': 'Shalini1234567890', 'age': 30}), schema)
        print(v.errors)

        #Allowing the unknown
        v.allow_unknown = True
        print("\nAllowing the unknowns: ", v.validate({'name': 'Shalini', 'age': 30}), schema)

        # allowing the unknown with specific type
        v.allow_unknown = {'type': 'integer'}
        print("\nAllowing the unknowns with specific type: ", v.validate({'name': 'Shalini', 'age': 30}), schema)

        #checking the allowed
        v.schema = {'role':{'type':'list', 'allowed':['developer', 'tester', 'engineer']}}
        print('\nchecking tha \'allowed\' thing: ', v.validate({'role': ['abc']}))
        print(v.errors)


        #Dependenciess
        schema1 = {'profession': {'type':'string', 'required': False},
                    'experience': {'required': True,
                                  'dependencies': {'profession':['developer', 'tester']}
                                  }
                   }
        v1 = Validator(schema1)
        print('\n Testing dependencies: ', v1.validate({'profession':'tester'}))
        print(v1.errors)



        # validate allowed unknowns also
        # v.allow_unknown = {'age': {'type':'int','anyof': [{'value': 10}, {'value': 20}]}}
        # print("Validating te allowed unknowns: ", v.validate({'name': 'Shalini', 'age': 10}), schema)
        # print(v.errors)
        # print("Validating te allowed unknowns: ", v.validate({'name': 'Shalini', 'team': 'Jedi'}), schema)
        # print(v.errors)

        # allowed_unknown we can apply on nested schema
        # e.g. dict inside schema or schema inside schema

        #validated method???




c = cerberusTest()