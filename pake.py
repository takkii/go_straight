# Run, unit/xunit.py

print('----------------------------------------------------------------------')

with open('./unit/xunit.py') as xut:
    xcmd = xut.read()
    exec(xcmd)

print('----------------------------------------------------------------------')

# Run, unit/unit.py

with open('./unit/unit.py') as ut:
    cmd = ut.read()
    exec(cmd)
