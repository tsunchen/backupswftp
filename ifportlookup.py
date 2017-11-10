#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pysnmp.entity.rfc3413.oneliner import cmdgen



ifPort = {}

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
            errorIndication, errorStatus, errorIndex, varBinds = self.cg.getCmd( 
                cmdgen.CommunityData('Agent', self.community, self.version),
                cmdgen.UdpTransportTarget((self.destHost, 161)),
                self.mid
            ) 
            result = varBinds[0][1]
        except Exception, err:
            print err
            result = None
        return result

def runit(loop=1):
    for i in range(loop):
        s = Snmppyget('publ1c', '211.152.50.254', '1.3.6.1.2.1.1.5.0')
        hostname = s.query()
        while ((hostname) == None):
            print  (hostname)
            s = Snmppyget('publ1c', '211.152.50.254', '1.3.6.1.2.1.1.5.0')
            hostname = s.query()
        print hostname
        hostname = str(hostname)
        ifPort['hostname'] = hostname

        s = Snmppyget('publ1c', '211.152.50.254', '1.3.6.1.2.1.2.2.1.2.15')
        ifDesc = s.query()
        while ((ifDesc) == None):
            print  (ifDesc)
            s = Snmppyget('publ1c', '211.152.50.254', '1.3.6.1.2.1.2.2.1.2.15')
            ifDesc = s.query()
        print ifDesc
        ifDesc = str(ifDesc)
        ifPort['ifDesc'] = ifDesc

        s = Snmppyget('publ1c', '211.152.50.254', '1.3.6.1.2.1.2.2.1.10.15')
        ifIn = s.query()
        while ((ifIn) == None):
            print  ifIn
            s = Snmppyget('publ1c', '211.152.50.254', '1.3.6.1.2.1.2.2.1.10.15')
            ifIn = s.query()
        print ifIn
        ifIn = int(ifIn)
        ifPort['ifIn'] = ifIn

        s = Snmppyget('publ1c', '211.152.50.254', '1.3.6.1.2.1.2.2.1.16.15')
        ifOut = s.query()
        while ((ifOut) == None):
            print  ifOut
            s = Snmppyget('publ1c', '211.152.50.254', '1.3.6.1.2.1.2.2.1.16.15')
            ifOut = s.query()
        print ifOut
        ifOut = int(ifOut)
        ifPort['ifOut'] = ifOut

        s = Snmppyget('publ1c', '211.152.50.254', '1.3.6.1.2.1.2.2.1.5.15')
        ifSpd = s.query()
        while ((ifSpd) == None):
            print  ifSpd
            s = Snmppyget('publ1c', '211.152.50.254', '1.3.6.1.2.1.2.2.1.5.15')
            ifSpd = s.query()
        print ifSpd
        ifSpd = int(ifSpd)
        ifPort['ifSpd'] = ifSpd

        ifInPortflow = ifIn * 8 * 100 / ifSpd
        ifOutPortflow = ifOut * 8 * 100 / ifSpd
        ifPort['ifIn'] = ifInPortflow
        ifPort['ifOut']= ifOutPortflow
        ifPort['status'] = 0

        print  ifPort
        return  ifPort
        #print i

if __name__ == "__main__":
    runit(loop=2)
