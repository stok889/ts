import os
import subprocess
import shlex
import sys

wd = 'd:/ws/algorithms-manual/chapter-1'
td = 'test'

def testfile(fn: str):
    lt = os.listdir(wd + '/' + td)
    lf = [f for f in lt if 'in' in f]
    la = [f for f in lt if 'out' in f]
    ef = wd + '/' + fn
    for f in lf:
        file = td + '/' + f
        proc = subprocess.run(shlex.split('python ' + ef + ' ' + file), stdout = subprocess.PIPE)
        line = proc.stdout
        print(line.rstrip())

if __name__ == "__main__":
    if len(sys.argv[1]) < 1:
        print('Provide source file')
    else:
        testfile(sys.argv[1])