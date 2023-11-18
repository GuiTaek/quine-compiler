from runpy import run_path
def func(code, input_):
    return code + input_

old_func = func
with open("recursion_from_sample3.py", mode="r") as f:
    my_code = f.read()
exec(my_code)
input_ = "hello"
print(old_func(my_code, input_) == func(input_))
