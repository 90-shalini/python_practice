def func(x):
    print("In func function....")
    return x+1


def test_func():
    print('pytest is running')
    assert func(3) == 5



