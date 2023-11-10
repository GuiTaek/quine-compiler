import sys
import io
import argparse
from runpy import run_path

parser = argparse.ArgumentParser(
    prog="check_quine.py",
    description="Checks a python file by running it if it is a quine. If it's not"
                " a quine, then it prints out some helpful debugging infos.")
parser.add_argument("filename", help="the path to the file to check")
parser.add_argument("-l", "--log", dest="log", help="logs the output of the quine into this file. Defaults to not logging")
parser.add_argument("-w", "--window", dest="window", help="the window to show around the first difference when the code is no quine", type=int, default=20)
args = parser.parse_args()
WINDOW = args.window
old_stdout = sys.stdout
file_stdout = io.StringIO()
sys.stdout = file_stdout
run_path(args.filename)
sys.stdout = old_stdout
with open(args.filename, mode="r") as f:
    file_content = f.read()
output_content = file_stdout.getvalue()
if args.log:
    with open(args.log, mode="w") as f:
        f.write(output_content)
is_quine = file_content == output_content
print(f"{is_quine=}")
if not is_quine:
    differences = [ind for ind, (a, b) in enumerate(zip(file_content, output_content)) if a != b]
    if len(differences) > 0:
        ind = differences[0]
        print("first difference here:")
        start_ind = max(0, ind - WINDOW)
        end_ind = min(len(file_content) - 1, len(output_content) - 1, ind + WINDOW)
        print(f"  {file_content[start_ind: end_ind]=}")
        print(f"{output_content[start_ind: end_ind]=}")
    else:
        print(f"{len(file_content)=}")
        print(f"{file_content[-WINDOW:].encode()=}")
        print(f"{len(output_content)=}")
        print(f"{output_content[-WINDOW:].encode()=}")
