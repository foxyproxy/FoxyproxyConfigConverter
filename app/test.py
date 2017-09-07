#!/usr/bin/env python2

import os
import pprint
import foxyconvert as fc

testf = 'foxyproxy.xml'

def main():
    if os.path.isfile(testf):
        confobj = fc.conf()
        with open(testf, 'r') as f:
            confobj.getXML(f.read())
        confobj.parseXML()
        with open('foxyproxy.json', 'w') as f:
            f.write(confobj.giveJSON())

if __name__ == '__main__':
    main()
