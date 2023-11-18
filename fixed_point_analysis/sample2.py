from test_fixpoint import test_fixpoint, func
def func(string):
    return "´" + string

fixpoint = ""
print(fixpoint)
print(func(fixpoint))
assert test_fixpoint(func, fixpoint)