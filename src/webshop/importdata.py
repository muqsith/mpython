import os

dirname = os.path.dirname(__file__)

dirPath = os.path.join(dirname, '../../tmp/domainsdata')

for f in os.listdir(dirPath):
    domainName = f.replace('.json', '')
    filePath = os.path.realpath(os.path.join(dirPath, f))
    if os.path.isfile(filePath):
        os.system('cat ' + filePath + ' | /home/mui/one/wsdocker/webshopbackend/server/bin/webshop-data.js import ' + domainName + ' --config /home/mui/one/wsdocker/webshopbackend/config/development.cjson')