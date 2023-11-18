from runpy import run_path
for i in range(1, 4):
    try:
        run_path(f"never_compiling{i}.py")
    except SyntaxError:
        continue
    assert False