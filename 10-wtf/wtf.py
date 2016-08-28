import sys
import subprocess
import urllib2
import urllib
import re

try:
    import stackit
except:
    print ('require stackit')

# alias ???='python /path/to/wtf.py $(fc -ln -1 | tail -n 1);'

STACKIT_COMMAND = 'stackit -s "%s"'

def _main():
    command =  ' '.join(sys.argv[1:])
    try:
        o = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError, e:
        o = e.output

    errs    = []
    outputs = o.split('\n')
    find    = -1
    for i, err in enumerate(outputs):
        if not err.startswith(' ') and not err.startswith('Traceback'):
            find = i
            break
    if find == -1:
        return
    errs = ''.join(outputs[i:])
    
    command = STACKIT_COMMAND % errs
    subprocess.call(command, shell=True)

if __name__ == '__main__':
    _main()
