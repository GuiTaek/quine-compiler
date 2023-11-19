code = "placeholder"

import re
import ast
# this program doesn't support other whitespaces than " "
while_regex = re.compile("^( *)while (.*):$")
break_regex = re.compile("^( +)break$")
empty_line_regex = re.compile("^ *(#.*)?$")
other_line_regex = re.compile("^( *).*$")
lines = code.split("\n")
for ind1, line1 in enumerate(lines):
    if regex_res := while_regex.match(line1):
        if not ast.literal_eval(regex_res.group(2)):
            continue
        nr_spaces = len(regex_res.group(1))
        while_good = False
        for line2 in lines[ind1 + 1:]:
            # python match doesn't support regex and
            # I don't want a requirements.txt just for an example
            if regex_res2 := break_regex.match(line2):
                if len(regex_res2.group(1)) >= nr_spaces:
                    while_good = True
                    break
                else:
                    break
            if empty_line_regex.match(line2):
                continue
            regex_res2 = other_line_regex.match(line2)
            if len(regex_res2.group(1)) < nr_spaces:
                break
        if not while_good:
            # the unneccassary -1+1 hints at the two effects that cancel each other:
            # the first being the changes by quine_compiler.py and the second
            # being python starting to count on 0
            raise RuntimeError(f"Found bad while at line {(ind1-1) + 1}")

# do some random stuff
my_list = [1, 2, 3, 4, 5]
my_sum = 0
for elem in my_list:
    my_sum += elem * (elem - 1)
print(my_sum)

# now, there is an endless loop
break_now = True
while True:
    print("hello world")
    if break_now:
        break_now = False
        # error, should be break
        continue

# now, a some good whiles
while False:
    print("I'm never reached :(")

while "":
    print("I'm also never reached!")