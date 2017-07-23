#
# destination ftp 
#
# copy startup-config
#
# www.tsunchen.com/ftp/tscisco/
#




# -*- coding: utf-8 -*-
from sys import argv
import telnetlib

import threading

def telnetswftp(host, ip, username, password, enable_password):
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
     tn.write('ip ftp username tscisco.copyrun' + '\n')
     tn.write('ip ftp password Ccq480105_cisco' + '\n')
     tn.write('exit' + '\n')
     tn.write('copy startup-config ftp' + '\n')
     tn.write('50.62.160.81' + '\n')
     #tn.write(host + '.txt' + '\n')
     tn.write(host + '\n')
     tn.write('\n')
     tn.write('\n')
     tn.write('conf t' + '\n')
     tn.write('no ip ftp username tscisco.copyrun' + '\n')
     tn.write('no ip ftp password Ccq480105_cisco' + '\n')
     tn.write('exit' + '\n')
     tn.write('\n')
     tn.write('\n')
     tn.write('quit\n')
     temp = tn.read_all()
     print "%r", temp
     print 'Done!\n'

filename = 'E:/backupswitch/b-sw.ini'
sw_ini = open(filename)
countsw = 0

while 1:
  swcfg = sw_ini.readline()
  if swcfg :
      host , ip , username , password , enable_password = swcfg.split(':')
      print 'Start Backuping: '+ host
      #tn = telnetlib.Telnet(ip)
      #telnetswftp(host , ip , username , password , enable_password)
      t = threading.Thread(target=telnetswftp, args=(host , ip , username , password , enable_password))
      t.start()
      t.join()
      countsw += 1
  else:
      break

sw_ini.close()
print 'All switchers\' backuping completed!'
print 'Count of Backuped is %d '% countsw
