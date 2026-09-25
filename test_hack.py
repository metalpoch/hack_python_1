from hack_1 import fn_hack_1
from hack_2 import fn_hack_2
from hack_3 import fn_hack_3
from hack_4 import fn_hack_4
from hack_5 import fn_hack_5
from hack_6 import fn_hack_6
from hack_7 import fn_hack_7
from hack_8 import fn_hack_8
from hack_9 import fn_hack_9
from hack_10 import fn_hack_10


# h-1
def test_hack_1():
    v = fn_hack_1()
    ck_1 = isinstance(v, str)
    ck_2 = v == "FOOZIMAN"
    assert (ck_1, ck_2) == (True, True)


# h-2
def test_hack_2():
    v = fn_hack_2()
    assert v == "Hola Mundo"


# h-3
def test_hack_3():
    v = fn_hack_3()
    assert v == (13, 7, 30, 1, 3)


# h-4
def test_hack_4():
    v = fn_hack_4()
    assert v is True


# h-5
def test_hack_5():
    v = fn_hack_5()
    assert v == "Notable"


# h-6
def test_hack_6():
    v = fn_hack_6()
    assert v == "isosceles"


# h-7
def test_hack_7():
    v = fn_hack_7()
    assert v == [0, 1, 2, 3, 4, 5]


# h-8
def test_hack_8():
    v = fn_hack_8()
    assert v == [5, 4, 3, 2, 1, 0]


# h-9
def test_hack_9():
    v = fn_hack_9()
    assert v == [2, 4, 6]


# h-10
def test_hack_10():
    v = fn_hack_10()
    assert v == [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]
