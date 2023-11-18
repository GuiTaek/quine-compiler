code = r"code = f\"code = r\\\"{code}\\\"\\n\" + code.encode().decode(\"unicode_escape\")\n\ndef func(input_):\n    return code + input_"
code = f"code = r\"{code}\"\n" + code.encode().decode("unicode_escape")

def func(input_):
    return code + input_