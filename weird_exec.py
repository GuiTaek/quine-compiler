def test():
    code="a=0\ndef func(): print(a)"
    locals_ = {}
    exec(code, {}, locals_)
    locals_["func"]()
test()