#
# destination ftp
#
# copy startup-config
#
# www.tsunchen.com/ftp/tscisco/
#
# 12-Jan-2019 (F:\ProgramData\Anaconda2) C:\Users\Administrator>python e:\projects\python\pyswitcher\pyswitcher.py
# host:ip:username:password:enable_password:interfaceport:displayname:speedlimit:enable_line
#




#-*- coding: utf-8 -*-
from sys import argv
import telnetlib

import threading

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time


def telnetswUpdateSpeed10(host, ip, username, password, enable_password, interfaceport, displayname, speedlimit):
    tn = telnetlib.Telnet(ip)
    tn.read_until('Username: ')
    tn.write(username + '\n')
    tn.read_until('Password: ')
    tn.write(password + '\n')
    tn.write('enable' + '\n')
    tn.read_until('Password: ')
    tn.write(enable_password + '\n')
    tn.write('\n')
    tn.write('\n')
    tn.write('conf t' + '\n')
    print(ip)
    print(interfaceport)
    print(speedlimit)
    tn.write('interface ' + interfaceport + '\n')
    if (speedlimit == "0"):
        tn.write('no speed' + '\n')
    else:
        tn.write('speed  10' + '\n')
    tn.write('exit' + '\n')
    tn.write('exit' + '\n')
    tn.write('\n')
    tn.write('\n')
    tn.write('quit\n')
    temp = tn.read_all()
    print(temp)




def telnetswftp(host, ip, username, password, enable_password, interfaceport, displayname, speedlimit):
     tn = telnetlib.Telnet(ip)
     tn.read_until('Username: ')
     tn.write(username + '\n')
     tn.read_until('Password: ')
     tn.write(password + '\n')
     tn.write('enable' + '\n')
     tn.read_until('Password: ')
     tn.write(enable_password + '\n')
     tn.write('\n')
     tn.write('\n')
     #tn.write('conf t' + '\n')
     tn.write('show run interface ' + interfaceport)
     #tn.write('ip ftp username tscisco.copyrun' + '\n')
     #tn.write('ip ftp password Ccq480105_cisco' + '\n')
     #tn.write('exit' + '\n')
     #tn.write('copy startup-config ftp' + '\n')
     #tn.write('50.62.160.81' + '\n')
     #tn.write(host + '.txt' + '\n')
     #tn.write(host + '\n')
     tn.write('\n')
     tn.write('\n')
     #tn.write('conf t' + '\n')
     #tn.write('no ip ftp username tscisco.copyrun' + '\n')
     #tn.write('no ip ftp password Ccq480105_cisco' + '\n')
     #tn.write('exit' + '\n')
     tn.write('\n')
     tn.write('\n')
     tn.write('quit\n')
     temp = tn.read_all()
     print (">>> telnet %s hostname %s of [%s]" % (ip, host, displayname))
     if 'speed' in temp:
          print ("%s speed limit is") % (interfaceport)
          displayname=temp.index('speed')
          print ("!"+temp[displayname:displayname+12])
     else:
          print ("%s Speed is NO Limited") % (interfaceport)
          print(speedlimit)
          print(interfaceport)
          telnetswUpdateSpeed10(host, ip, username, password, enable_password, interfaceport, displayname, speedlimit)
          #update as speedlimit

     #print "%r", temp
     #print interfaceport
     #print displayname
     #print ('Done!\n')



#filename = 'E:/backupswitch/b-sw-share-netflow.ini'
filename='E:/tsun/BA-switcher/b-sw-share-netflow.txt'
sw_ini = open(filename)
countsw = 0

res_list = []

while 1:
  swcfg = sw_ini.readline()
  if swcfg :
      host , ip , username , password , enable_password, interfaceport, displayname, speedlimit, enable_line = swcfg.split(':')
      #print ('Start Scanning: '+ host)
      #tn = telnetlib.Telnet(ip)
      #telnetswftp(host , ip , username , password , enable_password)
      #t = threading.Thread(target=telnetswftp, args=(host , ip , username , password , enable_password))
      #t.start()
      #t.join()
      res_list.append(threading.Thread(target=telnetswftp, args=(host , ip , username , password , enable_password, interfaceport, displayname, speedlimit)) )
      countsw += 1
  else:
      break

sw_ini.close()

for i in res_list:
  i.start()

for i in res_list:
  i.join()
  if i.isAlive():
    print ('->>>: the threading %s has not done yet' %i)

print ('All switchers\' showing are completed!')
print ('count of scanning is %d '% countsw)
