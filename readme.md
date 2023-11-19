# what it does
It transforms a python file into another python file that knows its code. It doesn't make use of `eval()`, `exec()` or `open(__file__)`. This repo is probably more of academic interest.
# installation
Install the newest version of [Python](https://www.python.org/downloads/) and clone or download this repository. No there aren't any requirements, just plain Python.
# documentation
See
```python check_quine.py --help```,
```python quine_compiler.py --help```,
```python check_recursion.py --help``` and
```python recursion_compiler.py --help```
# automatic_quine_examples
## check_sure_endless_loop
Run
```python quine_compiler.py automatic_quine_examples/check_sure_endless_loop.py -fr```
## menu
Run
```python quine_compiler.py -o quine.py automatic_quine_examples/menu.py -f```
then
```python check_quine.py quine.py```
type in `quine` and then the output should be `is_quine=True`
## search_for_comment.py
```python quine_compiler.py automatic_quine_examples/search_for_comment.py -fr```
## n-quine.py
```python quine_compiler.py automatic_quine_examples/n-quine.py -fr```
then
```python check_quine.py quine.py```
type in `1` and then the output should be `is_quine=True`, then run above command again, type in `2` and then the output should be `is_quine=False`
# recursion_examples
It's difficult to write functions, that guarantee that the output is indeed a function, therefore only trivial examples. They all work the same way:

Let <path> be the path to a file in the folder recursion_examples, then run:
```python recursion_compiler.py <path> -f```
then
```python check_recursion.py <path> recursion.py <input-to-your-function>```
whilst printing the things your function prints two times, it should always print `test result: True`
# manual_quine_examples
these examples were just some playground to get the algorithm of the quine_compiler. If you want, you can
```
python check_quine.py manual_quine_examples/<filename>
```
where <filename> is replaced by the file you're interested in. Everyone should output `is_quine=True`

# fixed_point_analysis
these examples were just some playground to get the algorithm of recursion_compiler and a planned fixpoint_compiler. See [fixed point readme](https://github.com/GuiTaek/quine-compiler/blob/main/fixed_point_analysis/readme.md).