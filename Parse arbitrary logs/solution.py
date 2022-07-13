# Access log file to parse
# http://jascha.wesemann-gmbh.de/log/access.log
# Found via Google Dorks: intitle:index of "access.log"
import requests
import re

access_log = requests.get("http://jascha.wesemann-gmbh.de/log/access.log")
regex = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*\[(.*)].\"([^\"]*)\".(\d{3}).(\d{0,10}).\"([^\"]*)\".\"([^\"]*)\""
parsed = []


for line in access_log.text.split('\n'):
    match = re.search(regex, line, re.IGNORECASE)
    if match:
        ip,timestamp,query,status_code,size,directory,useragent = match.group(1),match.group(2),match.group(3),match.group(4),match.group(5),match.group(6),match.group(7)
        parsed.append({'ip':ip,'timestamp':timestamp,'query':query,'status_code':status_code,'size':size,'directory':directory,'useragent':useragent})

print(parsed)