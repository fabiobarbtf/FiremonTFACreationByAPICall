##### Imports #####
import requests
import pandas as pd
import urllib3
from datetime import date, timedelta
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

##### Dataframes #####
tabela = pd.read_csv("Rules.csv", sep=",")
df = pd.DataFrame(tabela)
df_new = (df.iloc[:, [4,25]])
df_id = (df.iloc[:, [24]])
df_idenfifier = pd.DataFrame()


##### Rules Collection #####
with open("BaseRegras.txt", "r") as arquivo:
    rules = arquivo.readlines()
rules = [arquivo.strip('\n') for arquivo in rules]
_current = ''
for rule_name in rules:
    if rule_name != _current:
        row_number = df_new[df_new['rule.name'] == rule_name].index[0]
        rule_id = (df_id.iloc[[row_number]])
        df_idenfifier = pd.concat([df_idenfifier, rule_id], ignore_index=True)
id_list = (df_idenfifier['rule.identifier'].tolist())

def merge(id_list, rules):
    merged_list = [(id_list[i], rules[i]) for i in range(0, len(id_list))]
    return merged_list
merged_lists = (merge(id_list, rules))
today_date = date.today()


##### Goal Setting #####
print("""\
\033[1;31;40m  _____ _                                  _____ _____ _       ____                _             
\033[1;31;40m |  ___(_)_ __ ___ _ __ ___   ___  _ __   |_   _|  ___/ \     / ___|_ __ ___  __ _| |_ ___  _ __ 
\033[1;31;40m | |_  | | '__/ _ \ '_ ` _ \ / _ \| '_ \    | | | |_ / _ \   | |   | '__/ _ \/ _` | __/ _ \| '__|
\033[1;31;40m |  _| | | | |  __/ | | | | | (_) | | | |   | | |  _/ ___ \  | |___| | |  __/ (_| | || (_) | |   
\033[1;31;40m |_|   |_|_|  \___|_| |_| |_|\___/|_| |_|   |_| |_|/_/   \_\  \____|_|  \___|\__,_|\__\___/|_|                                            
""")
print('')

### User Report ###
user = input("""\
\033[1;31;40m Inform your Firemon User!
\033[1;32;40m  User:""")
print('')
time.sleep(0.50)
print(user)

### Password Report ###
password = input("""\
\033[1;31;40m Enter your Firemon Password!
\033[1;32;40m Password:""")
print('')
time.sleep(0.50)
print(password)

### Cluster Choice ###
cluster = input("""\
\033[1;31;40m Enter the Cluster Name (Without Spaces)!
\033[1;32;40m  Cluster:""")
print(f"\033[1;37;40m  The chosen cluster was: {cluster}")
print('')
time.sleep(0.50)

### IP choice ###
firemon_ip = input("""\
\033[1;31;40m Enter Firemon's IP!
\033[1;32;40m  IP:""")
print(f"\033[1;37;40m  IP Configured as: {cluster}")
print('')
time.sleep(0.50)

### Choosing DomainID ###
try:
    domainId = int(input("""\
\033[1;31;40m Enter the Domain ID!
        \033[1;33;40m Obs.: It must be an integer.
\033[1;32;40m  Domain ID:"""))
    print(f"\033[1;37;40m  The chosen DomainID was: {domainId}")
    print('')
except:
    print(f"\033[1;37;40m  The Value entered is not a DomainID! Restart the script!")
    print('')
    input()
    exit()
time.sleep(0.50)

### Choice of DeviceID ###
try:
    deviceId = int(input("""\
\033[1;31;40m Enter the Device ID!
        \033[1;33;40m Obs.: It must be an integer.
\033[1;32;40m  Device ID:"""))
    print(f"\033[1;37;40m  The chosen DeviceID was: {deviceId}")
    print('')
except:
    print(f"\033[1;37;40m  The Value entered is not a DeviceID! Restart the script!")
    print('')
    input()
    exit()
time.sleep(0.50)

### Choice of Duration ###
try:
    duration = int(input("""\
\033[1;31;40m Enter the TFA Duration!
        \033[1;33;40m Obs.: Only valid 1, 7 and 30
\033[1;32;40m  Duration:"""))
    if duration != 1 and duration != 7 and duration != 30:
        print(f"\033[1;37;40m  The Value entered is not a valid Duration! Restart the script!")
        print('')
        input()
        exit()
    print(f"\033[1;37;40m  The duration chosen was: {duration}")
    print('')
except:
    print(f"\033[1;37;40m  The Value entered is not a valid Duration! Restart the script!")
    print('')
    input()
    exit()
time.sleep(0.50)

##### End Date Setting #####
duration_time= timedelta(duration)
create = today_date
endDate = (today_date + duration_time)

##### Script Start Information #####
print("\033[1;31;40m 10 Seconds to Start the Script!!!")
print("\033[1;37;40m To cancel the script, simply close the script or press Ctrl+C on the script!")
print('')
time.sleep(10)

##### Creation of TFAs #####
print("\033[1;37;40m Script Started!")
print('')
api_url = (f'https://{firemon_ip}/securitymanager/api/domain/{domainId}/device/{deviceId}/trafficflow')
for id, name in merged_lists:
    if id != _current:
        TFAName = (f'{cluster}-{name}-{create}')
        data = {
            "domainId": domainId,
            "name": TFAName,
            "description": (f"Traffic flow for the rule: {name}"),
            "deviceId": deviceId,
            "ruleId": id,
            "duration": duration,
            "endDate": (f"{endDate}T00:00:00.000Z")
        }
        creation_response = requests.post (url=api_url, json=data, auth=(user, password), verify=False)
        if creation_response.status_code >= 200 and creation_response.status_code <- 299:
            print('---------------------------------------------------------------------')
            print('Rule: ', name)
            print('Status Code: ', creation_response.status_code)
            print('Reason: ', creation_response.reason)
        else:
            print('---------------------------------------------------------------------')
            print('Rule: ', name)
            print('Status Code: ', creation_response.status_code)
            print('Reason: ', creation_response.reason)
print("\033[1;37;40m Script Closed!")
input()
exit()
