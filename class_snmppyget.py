#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pysnmp.entity.rfc3413.oneliner import cmdgen

'''
class Snmp(object):
    """A basic SNMP session"""
    def __init__(self,oid="sysDescr", Version=2):
        self.oid = oid
        self.version = Version
        self.destHost = sys.argv[1]
        self.community = sys.argv[2]

    def query(self):
        """Creates SNMP query session"""
        try:
            result = netsnmp.snmpwalk(self.oid, Version = self.version, DestHost = self.destHost, Community = self.community)
        except Exception, err:
            print (err)
            result = None
        return result
'''


# reference python for linux and unix administration 
# pysnmp classification
class Snmppyget(object):
    """A basic SNMP session"""
    def __init__(self, Community, DestHost, MIB, Version=1):
        self.version = Version
        self.mid = MIB
        self.destHost = DestHost
        self.community = Community
        self.cg = cmdgen.CommandGenerator()

    def query(self):
        """Creates SNMP query session"""
        try:
            #cg = cmdgen.CommandGenerator()
            errorIndication, errorStatus, errorIndex, varBinds = self.cg.getCmd( 
                cmdgen.CommunityData('Agent', self.community, self.version),
                cmdgen.UdpTransportTarget((self.destHost, 161)),
                self.mid
            ) 
            result = varBinds[0]
        except Exception, err:
            print err
            result = None
        return result

def runit(loop=1):
    for i in range(loop):
        s = Snmppyget('pub', '211.152', '1.3.6.1.2.1.1.5.0')
        port = s.query()
        print port
        #print i

if __name__ == "__main__":
    runit(loop=1)
