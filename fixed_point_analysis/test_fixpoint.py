import sys
import io
# works only for the first example named sample1.py
# assert input via input() and output via print()
# according to the theorem of Rice, there is
# no way to test, if two arbitrary python codes
# are functionally the same, therefore the test_cases
func = None
def test_fixpoint(fixpoint_func, fixpoint):
    global func
    pre_func = fixpoint
    aft_func = fixpoint_func(fixpoint)
    result = []
    for point in [pre_func, aft_func]:
        old_stdout = sys.stdout
        file_stdout = io.StringIO()
        sys.stdout = file_stdout
        exec(point)
        result.append(file_stdout.getvalue())
        sys.stdout = old_stdout
    return result[0] == result[1]