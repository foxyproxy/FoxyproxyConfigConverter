#!/usr/bin/env python2

import argparse
import os
import pprint
import sys
import foxyconvert as fc

def parseArgs():
    args = argparse.ArgumentParser()
    args.add_argument(dest = 'conf',
                      metavar = 'path/to/foxyproxy.xml',
                      help = 'The path to your foxyproxy.xml file. See https://getfoxyproxy.org/configconverter for info on where to find this.')
    return(args)

def main():
    args = vars(parseArgs().parse_args())
    args['conf'] = os.path.abspath(os.path.expanduser(args['conf']))
    if os.path.isfile(args['conf']):
        confobj = fc.conf()
        newfile = os.path.join(os.path.dirname(args['conf']),
                               os.path.basename(args['conf']).replace('.xml', '.json'))
        with open(args['conf'], 'r') as f:
            if sys.version_info[0] < 3:  # python 2.6, 2.7
                confobj.getXML(f.read())
            else:
                confobj.getXML(f.read().encode('utf-8'))  # python 3
        confobj.parseXML()
        with open(newfile, 'w') as f:
            f.write(confobj.giveJSON())
        print(('The new configuration has been created at {0}.\n' +
               'Your old configuration ({1}) has been kept in-place.').format(newfile, args['conf']))

if __name__ == '__main__':
    main()
