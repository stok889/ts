import os
import sys

wd = 'd:/ws/algorithms-manual/chapter-1'
td = 'test'

def compare(f1: str, f2: str) -> int:
    ret = 0
    return ret

def runchecker(fn: str) -> str:
    ret = ''
    lt = os.listdir(wd + '/' + td)
    ltc = os.listdir(wd)
    lf = [f for f in lt if 'out' in f]
    lc = [f for f in ltc if 'out' in f]

    if len(lf) != len(lc):
        ret = 'Wrong number of tests'
    else:        
        for i in range(len(lf)):
            t = compare(lf[i], lc[i])
            if t == 0:
                ret = 'Test ' + str(i) + ' wrong answer'
                break

    return ret

if __name__ == '__main__':
    if len(sys.argv) < 1:
        print('Provide file\'s name for checking')
    else:
        print(runchecker(sys.argv[1]))