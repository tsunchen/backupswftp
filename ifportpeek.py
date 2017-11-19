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

def runit(loop, community, host, port):
    for i in range(loop):
        s = Snmppyget(community, host, '1.3.6.1.2.1.1.5.0')
        hostname = s.query()
        while ((hostname) == None):
            print  (hostname)
            s = Snmppyget(community, host, '1.3.6.1.2.1.1.5.0')
            hostname = s.query()
        print hostname
        hostname = str(hostname)
        ifPort['hostname'] = hostname

        ifDescMIB = '1.3.6.1.2.1.2.2.1.2.'
        ifDescMIB += port
        #print ifDescMIB
        s = Snmppyget(community, host, ifDescMIB)
        ifDesc = s.query()
        while ((ifDesc) == None):
            print  (ifDesc)
            s = Snmppyget(community, host, ifDescMIB)
            ifDesc = s.query()
        print ifDesc
        ifDesc = str(ifDesc)
        ifDescKey = 'ifDesc' + port
        ifPort[ifDescKey] = ifDesc

        ifInMIB = '1.3.6.1.2.1.2.2.1.10.'
        ifInMIB += port
        s = Snmppyget(community, host, ifInMIB)
        ifIn = s.query()
        while ((ifIn) == None):
            print  ifIn
            s = Snmppyget(community, host, ifInMIB)
            ifIn = s.query()
        print ifIn
        ifIn = int(ifIn)
        #ifInKey = 'ifIn' + port
        ifInKey = 'ifIn::' + ifDesc.replace("/","_")
        ifPort[ifInKey] = ifIn

        ifOutMIB = '1.3.6.1.2.1.2.2.1.16.'
        ifOutMIB += port
        s = Snmppyget(community, host, ifOutMIB)
        ifOut = s.query()
        while ((ifOut) == None):
            print  ifOut
            s = Snmppyget(community, host, ifOutMIB)
            ifOut = s.query()
        print ifOut
        ifOut = int(ifOut)
        #ifOutKey = 'ifOut' + port
        ifOutKey = 'ifOut::' + ifDesc.replace("/","_")
        ifPort[ifOutKey] = ifOut

        ifSpdMIB = '1.3.6.1.2.1.2.2.1.5.'
        ifSpdMIB += port
        s = Snmppyget(community, host, ifSpdMIB)
        ifSpd = s.query()
        while ((ifSpd) == None):
            print  ifSpd
            s = Snmppyget(community, host, ifSpdMIB)
            ifSpd = s.query()
        print ifSpd
        ifSpd = int(ifSpd)
        if (ifSpd == 0):
            ifSpd = 100000000 
        #ifSpdKey = 'ifSpd' + port
        ifSpdKey = 'ifSpd::' + ifDesc
        ifPort[ifSpdKey] = ifSpd

        ifInPortflow = ifIn * 8 * 100 / ifSpd
        ifOutPortflow = ifOut * 8 * 100 / ifSpd
        ifPort[ifInKey] = ifInPortflow
        ifPort[ifOutKey]= ifOutPortflow
        ifPort['status'] = 0

        #print  ifPort
        return  ifPort
        #print i

if __name__ == "__main__":
    runit(1, 'publ1c', '211.152.50.254', '1')
    runit(1, 'publ1c', '211.152.50.254', '2')
    runit(1, 'publ1c', '211.152.50.254', '3')
    runit(1, 'publ1c', '211.152.50.254', '4')
    runit(1, 'publ1c', '211.152.50.254', '5')
    runit(1, 'publ1c', '211.152.50.254', '6')
    runit(1, 'publ1c', '211.152.50.254', '7')
    runit(1, 'publ1c', '211.152.50.254', '8')
    runit(1, 'publ1c', '211.152.50.254', '9')
    runit(1, 'publ1c', '211.152.50.254', '10')
    runit(1, 'publ1c', '211.152.50.254', '11')
    runit(1, 'publ1c', '211.152.50.254', '12')
    runit(1, 'publ1c', '211.152.50.254', '13')
    runit(1, 'publ1c', '211.152.50.254', '14')
    runit(1, 'publ1c', '211.152.50.254', '15')
    runit(1, 'publ1c', '211.152.50.254', '16')
    runit(1, 'publ1c', '211.152.50.254', '17')
    runit(1, 'publ1c', '211.152.50.254', '18')
    runit(1, 'publ1c', '211.152.50.254', '19')
    runit(1, 'publ1c', '211.152.50.254', '20')
    runit(1, 'publ1c', '211.152.50.254', '21')
    runit(1, 'publ1c', '211.152.50.254', '22')
    runit(1, 'publ1c', '211.152.50.254', '23')
    runit(1, 'publ1c', '211.152.50.254', '24')
    runit(1, 'publ1c', '211.152.50.254', '25')
    print ifPort
