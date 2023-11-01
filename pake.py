import gc

try:
    print('---------------------------------------------------------------')

    # Run, unit/xunit.py
    with open('./unit/xunit.py') as xut:
        xcmd = xut.read()
        exec(xcmd)

    print('---------------------------------------------------------------')

    # Run, unit/unit.py
    with open('./unit/unit.py') as ut:
        cmd = ut.read()
        exec(cmd)

except Exception as ext:
    print(ext)
    raise RuntimeError from None

    # Custom Exception.
except ValueError as ext:
    print(ext)
    raise RuntimeError from None

finally:
    # GC collection.
    gc.collect()
