import argparse
import importlib.util
import os

from recursion_compiler import extract_func_name

def main():
    parser = argparse.ArgumentParser(
        prog="check_recursion.py",
        description="Checks if a recursion found by the recursion compiler is correct"
    )
    parser.add_argument(dest="functioncode", help="the file with the function to make recursive")
    parser.add_argument(dest="inputcode", help="the file with the function that is input into functioncode")
    parser.add_argument(metavar="input", dest="input_", help="the input to give into both functions. Use quotes (\") to input whitespaces")
    parser.add_argument("-w", "--window", dest="window", help="the window of characters which is shown on the first difference", default=30, required=False)
    parser.add_argument("-t", "--tempfile", dest="tempfile", help="the tempfile that is used to import the modules. exec can't be used easily, because the recursion needs global variables.", default="temp.py")
    args = parser.parse_args()
    with open(args.functioncode, mode="r") as f:
        functioncode_content = f.read()
    with open(args.inputcode, mode="r") as f:
        inputcode_content = f.read()
    func_name_1 = extract_func_name(functioncode_content)
    func_name_2 = extract_func_name(inputcode_content)
    assert (func_name:=func_name_1) == func_name_2
    print("test result:", test_recursion(func_name, functioncode_content, inputcode_content, args.input_, args.tempfile, args.window))

def load_function(module_name, filename, content):
    if os.path.exists(filename):
        raise RuntimeError(f"temp filename named {filename} already exists")
    with open(filename, mode="w") as f:
        f.write(content)
    # from ChatGPT
    # I don't know, what module_name exactly does, but I guess when it's set to
    # a constant value, there are name clashes possible
    spec = importlib.util.spec_from_file_location(module_name, filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    os.remove(filename)
    return module
def show_error(old_part, new_part, func_name):
    print(f"different part in {func_name}(code, input_):\n{old_part}")
    print(f"different part in {func_name}(input_):\n{new_part}")
def test_recursion(func_name, function_code, code, input_, temp_filename, window):
    old_locals = {}
    new_locals = {}
    
    old_func_lib = load_function("old_func_lib", temp_filename, function_code)
    new_func_lib = load_function("new_func_lib", temp_filename, code)
    
    old_result = getattr(old_func_lib, func_name)(code, input_)
    new_result = getattr(new_func_lib, func_name)(input_)
    if old_result == new_result:
        return True
    diff_inds = [ind for ind, (c1, c2) in enumerate(zip(old_result, new_result)) if c1 != c2]
    if diff_inds:
        diff_ind = diff_inds[0]
        start_ind = max(0, diff_ind - window)
        end_ind = diff_ind + window
        show_error(old_result[start_ind:end_ind], new_result[start_ind:end_ind])
    else:
        show_error(old_result[-window:], new_result[-window:])
    return False

if __name__ == "__main__":
    main()
