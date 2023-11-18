# aim of this folder
Create a fixed point generator, that takes in python code and generates a fixed point out of it, where a "fixed point" is a fixed point in the sense of [Kleene's first recursion theorem](https://en.wikipedia.org/wiki/Kleene%27s_recursion_theorem).
# sample 1
From sample 1, we learn, that it's possible to define fixpoints of python functions

# sample 2
From sample 2 and the folder never_compiling, we learn, that there are some functions, that don't have a fixed point. See [this](https://dev.to/lavary/how-to-fix-syntaxerror-invalid-character-in-python-28ie) for reasons why this never compiles. The reason why this is possible while the function is still total and computeable and the Kleene's fixed point theorem still holds is, that the fixed point theorem assumes every number to be a valid program, which is not the case for python programs. So from now on, we have to assume, that the function 1st) always terminates and 2nd) always output a correct python program.

# sample 3
From sample 3 we learn, that it's much easier to solve the equivalent [second recursion theorem](https://en.wikipedia.org/wiki/Kleene%27s_recursion_theorem#Kleene's_second_recursion_theorem) which can be reduced to the first recusion theorem.