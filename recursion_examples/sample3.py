# input is of form f"{oldvar}->{newvar}" and replaces every occurance of
# oldvar to newvar

#FUNC(func)
def func(code, input_):
    oldvar, newvar = input_.split("->")
    return code.replace(oldvar, newvar)