"""automatically create a command line tool out of a function with signature:
compile(placeholder:str, content:str)->str
usage -- include following code into your module without any non-defining code (e.g. `print("hello world")`):
```from default_compiler import run

if __name__ == "__main__":
    run(compile, "my_default_output_filename.py", "this is my funny compiler")```"""
import os
import argparse
def create_default_parser(default_output_filename, description):
    parser = argparse.ArgumentParser(
        prog="quine_compiler.py",
        description=description)
    parser.add_argument("-p", "--placeholder", dest="placeholder", help="the placeholder which defines"
                        " the string the variable in the input code is set to. Defaults to placeholder",
                        default="placeholder", required=False)
    parser.add_argument("-o", "--output", dest="outputfile", help="the output file", default=default_output_filename, required=False)
    parser.add_argument("inputfile", help="the file to process")
    parser.add_argument("-f", "--force", dest="force", help="overwrite the file given by -o. Defaults to"
                        " aborting on existing file.", action="store_true", required=False)
    parser.add_argument("-r", "--run", dest="run", help="not only compile, but also run the code", action="store_true", required=False)
    return parser
def default_compile_file(placeholder, inputfile, outputfile, force, run, compile_func):
    if os.path.exists(outputfile) and not force:
        raise RuntimeError(f"File \"{outputfile}\" already exists. Use -f if you want to overwrite")
    with open(inputfile) as f:
        content = f.read()
    result = compile_func(placeholder, content)
    with open(outputfile, mode="w") as f:
        f.write(result)
    if run:
        run_path(outputfile)
def run(compile_func, default_output_filename, description):
    parser = create_default_parser(default_output_filename, description)
    args = parser.parse_args()
    default_compile_file(args.placeholder, args.inputfile, args.outputfile, args.force, args.run, compile_func)
