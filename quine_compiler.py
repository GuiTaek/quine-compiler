import os
import re
import argparse
from runpy import run_path
def main():
    parser = argparse.ArgumentParser(
        prog="quine_compiler.py",
        description="Compiles a Python code to include"
        " its code into its source code. The compiler"
        " expects the first line to match the regex f'^([\w_]+) *= *(<placeholder>)'"
        " e.g. \nmy_code = \"placeholder\"\n"
        " where <placeholder> has the value inside the argument --placeholder")
    parser.add_argument("-p", "--placeholder", dest="placeholder", help="the placeholder which defines"
                        " the string the variable in the input code is set to. Default placeholder",
                        default="placeholder")
    parser.add_argument("-o", "--output", dest="outputfile", help="the output file", default="quine.py")
    parser.add_argument("inputfile", help="the file to process")
    parser.add_argument("-f", "--force", dest="force", help="overwrite the file given by -o. Defaults to"
                        " aborting on existing file.", action="store_true")
    parser.add_argument("-r", "--run", dest="run", help="not only compile, but also run the code", action="store_true")
    args = parser.parse_args()
    compile(args.placeholder, args.inputfile, args.outputfile, args.force, args.run)
def unescape(string):
    return string.encode('unicode_escape').decode().replace('"', r"\"")
def compile(placeholder, inputfile, outputfile, force, run):
    if os.path.exists(outputfile) and not force:
        raise RuntimeError(f"File \"{outputfile}\" already exists. Use -f if you want to overwrite")
    with open(inputfile) as f:
        lines = f.read().split("\n")
    regex = re.compile(f'^([\w_]+) *= *("{placeholder}")')
    if not (regex_res := regex.match(lines[0])):
        raise RuntimeError(f"Inputfile \"{inputfile}\" doesn't have correct format. First line has"
                           " to be e.g. \"my_code = \"placeholder\". See --help")
    var_name = regex_res.group(1)
    rest = "\n".join(lines[1:])
    second_line = f"{var_name} = f\"{var_name} = r\\\"{{{var_name}}}\\\"\\n\" + {var_name}.encode().decode(\"unicode_escape\")"
    first_line = f"{var_name} = r\"{unescape(second_line)}\\n{unescape(rest)}\""
    result = f"{first_line}\n{second_line}\n{rest}"
    with open(outputfile, mode="w") as f:
        f.write(result)
    if run:
        run_path(outputfile)

if __name__ == "__main__":
    main()
