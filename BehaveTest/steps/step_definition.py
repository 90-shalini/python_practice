from behave import *
from parse import *
from parse_type import TypeBuilder



class step_definitons:

    def __init__(self):
        pass

    @Given('I go to the meeting')
    def given_step_impl(context):
        print('>>>>>> In given step implementation')


    # parsing with split and making as list
    def parse_list(parameters):
        param_list = parameters.split(",")
        # param_list = TypeBuilder.with_one_or_more(parameters, listsep=",")
        return param_list
    register_type(List=parse_list)

    @When('I meet {persons:List}')
    def step_impl(context, persons):
        print(">>>>> Step Implementation of list of parameters")
        for person in persons:
            print("Met with people: ", person)

    @When(u'I want to meet {a+}{names}')
    def step_impl(context, names):
        print(">>>>> Implementing cardinality.")
        print(type(names))
        for name in names:
                print('want to meet ppl: ', name)

   # getting list using make choice predefined
    parse_list = TypeBuilder.make_choice(["Alice", "Bob", "Charly", "Dodo"])
    # register_type(mylist=parse_list)
    list_input = TypeBuilder.with_one_or_more(parse_list, listsep=",")
    register_type(list_names=list_input)

    @When('I test cardinality with {names:list_names}')
    def step_impl(context, names):
        print(">>>>> Step Implementation of list of parameters with TypeBuilder")
        print(type(names))
        for name in names:
            print(">>>>>> Names in list: ", name)

























            # # Making list with TypeBuilder.make_list NOT WORKING
            # def parse_names(input_params):
            #     print(">>>>> Parsing names using TypeBuilder")
            #     print(type(input_params))
            #     # parse_names_list = TypeBuilder.make_list(input_params, listsep=",")
            #     parse_names_list = TypeBuilder.with_many(input_params, listsep=",")
            #     schema = "{entry}"
            #
            #     print(type(parse_names_list))
            #     return parse_names_list
            #
            # register_type(list_names=parse_names)

    # def parse_dict(dict_input):
    #     print(type(dict_input))
    #     return dict
    # register_type(Dict=parse_dict)
    #
    # @When('my details {details:Dict}')
    # def dict_step_imp(context, details):
    #     print(">>>>> Step Implementation of dict of parameters")
    #     for key in details:
    #         print("Details: ", key)

