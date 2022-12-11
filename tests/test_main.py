# test_main.py

import hello_world_package as hwp


def test_hello(capfd):
    hwp.hello.say_hello()
    out, err = capfd.readouterr()
    assert out == "Hello World!\n"


def test_calculation():
    ans = 18
    out = hwp.calculate.do_calculation()
    assert out == ans
