from behave import *
from features import *


@Given('we have behave installed')
def step_impl(context):
    print('In given step')


@When('we implement a test')
def step_impl(context):
    context.execute_steps('''
                When we implement a test1
                ''')
    assert True is not False
    print('In When step')


@When('we implement a test1')
def step_impl(context):
    assert True is not True
    print('In When step-2')


@Then('behave will test it for us! "{text}"')
def step_impl(context, text):
    assert context.failed is False
    print('In Then step', text)