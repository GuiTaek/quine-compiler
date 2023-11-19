var0 = r"var"
var1 = r"var_list = [var0, var1]\nfor i, var in enumerate(var_list):\n    print(f'var{i} = r\"{var}\"')\nprint(var1.encode().decode(\"unicode_escape\"))"
var_list = [var0, var1]
for i, var in enumerate(var_list):
    print(f'var{i} = r"{var}"')
print(var1.encode().decode("unicode_escape"))
