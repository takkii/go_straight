with open('./unit/test_run.py') as ut:
    cmd = ut.read()
    exec(cmd)
