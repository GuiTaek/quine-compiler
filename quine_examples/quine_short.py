var = r"print(f'var = r\"{var}\"')\nprint(var.encode().decode(\"unicode_escape\"))"
print(f'var = r"{var}"')
print(var.encode().decode("unicode_escape"))
