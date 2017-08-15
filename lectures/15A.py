def test_function(t_num):
    print("inside")
    print(t_num, id(t_num))

    t_num = 4

    print("after changing value")
    print(t_num, id(t_num))

def my_function():
    test_num = 10
    print("Before calling")
    print(test_num)

    print("calling")
    test_function(test_num)

    print("after calling")
    print(test_num, id(test_num))

my_function()
