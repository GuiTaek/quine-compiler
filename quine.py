my_code = r"my_code = f\"my_code = r\\\"{my_code}\\\"\\n\" + my_code.encode().decode(\"unicode_escape\")\nuser_in = input()\nmatch user_in:\n    case \"hello\":\n        print(\"hello world\")\n    case \"quine\":\n        print(end=my_code)\n    case \"reverse\":\n        print(end=\"\".join(list(reversed(my_code))))\n    case _:\n        print(\"no case selected!\")"
my_code = f"my_code = r\"{my_code}\"\n" + my_code.encode().decode("unicode_escape")
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