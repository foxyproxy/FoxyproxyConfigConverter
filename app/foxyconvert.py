#!/usr/bin/env python2

import json
import re
try:
    from lxml import etree
    lxml_avail = True
except ImportError:
    import xml.etree.ElementTree as etree  # https://docs.python.org/2/library/xml.etree.elementtree.html
    lxml_avail = False

    
class conf(object):
    def __init__(self):
        pass

    def getXML(self, data):
        # Returns an XML object we can operate on.
        self.xmlobj = etree.fromstring(data)
        return(self.xmlobj)
    
    def parseXML(self):
        self.d = {'mode': self.xmlobj.get('mode')}
        for p in self.xmlobj.findall('proxies/proxy'):
            manualconf = p.find('manualconf')
            id = p.get('id')
            address = manualconf.get('host')
            port = manualconf.get('port')
            ptype = None
            # Get the type of proxyxml = 
            for a in p.keys():
                if a in ('isSocks', 'isHttps'):
                    if p.get(a).lower() in ('yes', 'true', '1'):
                        if a == 'isSocks':
                            sver = p.get('socksversion')
                            ptype = 'socks{0}'.format(sver)
                            break
                        elif a == 'isHttps':
                            ptype = 'https'
                            break
            index = p.get('selectedTabIndex')
            username = manualconf.get('username')
            password = manualconf.get('password')
            title = p.get('name')
            color = p.get('color')
            active = p.get('enabled')
            whitepatterns = []
            blackpatterns = []
            for ptrn in p.findall('matches/match'):
                protod = {'all': 1,
                          'http' : 2,
                          'https': 4}
                urilst = ptrn.get('pattern').split(':', 1)
                if len(urilst) > 1:
                    pregex = urilst[0].lower()
                else:
                    pregex = 'all'
                if len(urilst) > 1:
                    purl = urilst[1].lower()
                else:
                    purl = urilst[0].lower()
                if pregex not in ('http', 'https'):
                    pregex = 'all'
                purl = re.sub('^//', '', purl)
                if ptrn.get('isRegEx').lower() in ('yes', 'true', '1'):
                    isregex = 'regex'
                else:
                    isregex = 'wildcard'
                ptrnd = {'name': ptrn.get('name'),
                         'active': ptrn.get('enabled'),
                         'pattern': purl,
                         'type': isregex,
                         'protocols': protod[pregex]}
                if ptrn.get('isBlackList').lower() in ('yes', 'true', '1'):
                    blackpatterns.append(ptrnd)
                else:
                    whitepatterns.append(ptrnd)
            # And the catch-alls
            if not ptype:
                ptype = 'http'
            if address == '' or p.get('mode') == 'direct':
                ptype = 'direct'
            
            self.d[id] = {'address': address,
                          'port': port,
                          'type': ptype,
                          'index': int(index),
                          'username': username,
                          'password': password,
                          'title': title,
                          'color': color,
                          'active': active,
                          'whitePatterns': whitepatterns,
                          'blackPatterns': blackpatterns}
        return(self.d)
    
    def giveJSON(self):
        self.jsondump = json.dumps(self.d, sort_keys = True, indent = 4)
        return(self.jsondump)

def main(data):
    #return()  # comment out for running
    confobj = conf()
    confobj.getXML(data)
    confobj.parseXML()
    jsonobj = confobj.giveJSON()
    return(jsonobj)

if __name__ == '__main__':
    main(data)
