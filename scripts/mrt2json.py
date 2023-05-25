import json
import sys
from mrtparse import *

def main():
    sys.stdout.write('[\n')
    i = 0
    mrtData = ''
    for entry in Reader('rib.20160628.1600.bz2'):
        if i != 0:
            sys.stdout.write(',\n')
            mrtData += ',\n'
        mrtData += (json.dumps([entry.data], indent=2)[2:-2]) 
        sys.stdout.write(json.dumps([entry.data], indent=2)[2:-2])
        i += 1
    sys.stdout.write('\n]\n')
    sys.stdout.write(str(i))

    with open('mrt.json','w') as mrt:
        mrt.write(mrtData)

if __name__ == '__main__':
    main()