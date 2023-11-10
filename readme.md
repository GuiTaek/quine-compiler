# what it does
It transforms a python file into another python file that knows its code. It doesn't make use of `eval()`, `exec()` or `open(__file__)`. This repo is probably more of academic interest.
# installation
Install the newest version of [Python](https://www.python.org/downloads/) and clone or download this repository. No there aren't any requirements, just plain Python.
# documentation
See
```python check_quine.py --help
```
and
```python quine_compiler.py --help```
# examples
## check_sure_endless_loop
Run
```
python quine_compiler.py examples/check_sure_endless_loop.py -fr
```
## menu
Run
```
python quine_compiler.py -o quine.py examples/menu.py -f
```
then
```
python check_quine.py quine.py
```
type in `quine` and then the output should be `is_quine=True`
## search_for_comment.py
```
python quine_compiler.py examples/check_sure_endless_loop.py -fr
```
# quine_examples
these examples were just some playground to get the algorithm. If you want, you can
```
python check_quine.py quine_examples/<filename>
```
where <filename> is replaced by the file you're interested in. Everyone should output `is_quine=True`