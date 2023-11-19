import os
import re
import argparse
from runpy import run_path

from default_compiler import run

DESCRIPTION = "Compiles a Python code to include its code into its source code. The compiler expects the first line to match the regex f'^([\w_]+) *= *(<placeholder>)' e.g. \nmy_code = \"placeholder\"\n where <placeholder> has the value inside the argument --placeholder"

def unescape(string):
    return string.encode('unicode_escape').decode().replace('"', r"\"")

def quine_compile(placeholder, content):
    lines = content.split("\n")
    regex = re.compile(f'^([\w_]+)(:str)? *= *("{placeholder}")')
    if not (regex_res := regex.match(lines[0])):
        raise RuntimeError("Input parameter 'content' has wrong format.")
    var_name = regex_res.group(1)
    rest = "\n".join(lines[1:])
    second_line = f"{var_name} = f\"{var_name} = r\\\"{{{var_name}}}\\\"\\n\" + {var_name}.encode().decode(\"unicode_escape\")"
    first_line = f"{var_name} = r\"{unescape(second_line)}\\n{unescape(rest)}\""
    return f"{first_line}\n{second_line}\n{rest}"    

if __name__ == "__main__":
    run(quine_compile, "quine.py", DESCRIPTION)
