#!/usr/bin/python
import rrdtool

'''
rrdb=rrdtool.create('rest.rrd','--step','60','--start','1369982786',
    'DS:input:GAUGE:120:U:U',
    'DS:output:GAUGE:120:U:U',
    'RRA:LAST:0.5:1:600',
    'RRA:AVERAGE:0.5:5:600',
    'RRA:MAX:0.5:5:600',
    'RRA:MIN:0.5:5:600')
if rrdb:
  print rrdtool.error()
'''


rrd_9440 = rrdtool.create('w-2924-24-ct-08-share-50_traffic_in_9440.rrd','--step','300',
    '--start','N',
    'DS:traffic_in:COUNTER:600:0:100000000',
    'DS:traffic_out:COUNTER:600:0:100000000',
    'RRA:AVERAGE:0.5:1:600',
    'RRA:AVERAGE:0.5:6:700',
    'RRA:AVERAGE:0.5:24:775',
    'RRA:AVERAGE:0.5:288:797',
    'RRA:MAX:0.5:1:600',
    'RRA:MAX:0.5:6:700',
    'RRA:MAX:0.5:24:775',
    'RRA:MAX:0.5:288:797'
    )
if rrd_9440:
    print (rrdtool.error())
