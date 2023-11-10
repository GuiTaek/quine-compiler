var = r"var = f'var = r\"{var}\"\\n' + var.encode().decode(\"unicode_escape\")\nprint(end=var)\nimport winsound\nwinsound.Beep(300, 500)\n"
var = f'var = r"{var}"\n' + var.encode().decode("unicode_escape")
print(end=var)
import winsound
winsound.Beep(300, 500)
