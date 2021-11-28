################### DJANGO SETUP START ################### 
import os,sys,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "unchained.settings")
sys.path.extend(['/home/prajwal/gitlib/ct-home/unchained'])
django.setup()
#################### DJANGO SETUP END #################### 

import requests
from datetime import datetime as dt
from ip_interface.models import IP_Records

server_record = IP_Records.objects.values().order_by('-id')[0]
latest_ip = requests.get('http://ifconfig.me')
if not latest_ip.status_code == 200:
    print('Couldn\'t connect to the remote server')
    exit(1)

ip = latest_ip.text
server_ip = server_record['ip']

if (ip == server_ip): 
    id              =   server_record['id']
    count           =   server_record['count']

    record = IP_Records.objects.get(id=id)

    record.last_checked = dt.now()
    record.count = count+1
    update = record.save()
else:
    now = dt.now()
    update = IP_Records.objects.create(ip=ip).save()
