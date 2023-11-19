"""only supports variable names with english letters, numbers and underscores"""

import re

from quine_compiler import quine_compile
from default_compiler import run

def extract_func_name(content):
    regex_func_name = re.compile(r"#FUNC\(([a-zA-Z_0-9]+)\)")
    # it makes sense to use the last occuring #FUNC(), therefore the findall
    func_name = regex_func_name.findall(content)[-1]
    return func_name

def recursion_compile(placeholder, content):
    func_name = extract_func_name(content)
    # print(f"{func_name=}")
    # print(f"{variables=}") # don't need? remove at the end
    #assert content.count(func_name) == 1
    regex_func_extract = re.compile(rf"^(.*)( *def +{func_name} *\(([a-zA-Z_0-9]+) *(: *str *)?, *([a-zA-Z_0-9]+) *(: *str *)?\) *:)(.*)$", re.DOTALL)
    #                                    ^       ^                        ^            ^            ^                   ^             ^
    #                                    1st     2nd                     3rd          4th          5th                 6th           7th
    #print(f"{regex_func_extract.findall(content)=}")
    regex_res = regex_func_extract.match(content)
    before = regex_res.group(1)
    code_var = regex_res.group(3)
    if regex_res.group(4):
        code_var += regex_res.group(4)
    input_param = regex_res.group(5)
    if regex_res.group(6):
        input_param += regex_res.group(6)
    after = regex_res.group(7)
    quine_code = quine_compile(placeholder, f'{code_var}="{placeholder}"\n{before}def {func_name}({input_param}):{after}')
    return quine_code


if __name__ == "__main__":
    run(recursion_compile, "recursion.py")
