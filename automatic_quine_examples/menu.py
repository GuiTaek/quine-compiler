my_code = "placeholder"
user_in = input()
match user_in:
    case "hello":
        print("hello world")
    case "quine":
        print(end=my_code)
    case "reverse":
        print(end="".join(list(reversed(my_code))))
    case _:
        print("no case selected!")