#!/usr/bin/python

import json
import os
import sys
import yaml



#print 'Retreiving ambari server fqdn from ' + clusterConfigFilePath
with open('./conf.yaml', 'r') as cf:
	conf = yaml.safe_load(cf.read())

#print(conf)

node = []
for each_edge in conf['BDPInstall']:
     for value  in each_edge.values():
         node.append((value['edge_hostname'],value['BDP_custom_user']
         ))

print(node)

print(len(node))

nbHosts = len(node)
i = 1
fqdnStr = ''
for fqdn in node:
  fqdnStr = fqdnStr + fqdn[0] +','+ fqdn[1]
  if i < nbHosts:
    fqdnStr = fqdnStr + ';'
  i += 1

print(fqdnStr+';')
       
         

        
      





