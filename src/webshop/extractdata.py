import os
import json
import subprocess

dirname = os.path.dirname(__file__)

with open(os.path.join(dirname, '../../tmp/out.json'), 'r') as f:
   for line in f:
       d = json.loads(line)
       domainName = d["domain"]
       os.system('sudo /usr/lib/one.com-webshopbackend-app/server/bin/webshop-data export ' + domainName + ' > /home/mui/domainsdata/' + domainName + '.json')

f.close()
