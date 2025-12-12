# response codes and their meaning
# 1xx something like 102, 145 means hold up the final data is not yet received
# 2xx means this is the final data 
# 3xx permission denied
# 4xx you screwed up, there is no data to be found or it had been compromised
# 5xx the server screwed up

import requests
try:
    connection = requests.get('http://api.open-notify.org/iss-now.json')
    print(connection.status_code)
except connection.raise_for_status:
    print(connection.raise_for_status)
    
data = connection.json()
print(data)



