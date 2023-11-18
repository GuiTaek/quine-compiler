from test_fixpoint import test_fixpoint, func
def func(string):
    return string + "hello world"

fixpoint = "print('hello world')\n#"
assert test_fixpoint(func, fixpoint)