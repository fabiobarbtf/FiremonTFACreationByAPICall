########## IMPORTS ###########
import requests
import pandas as pd
from Rules import *

########## DATA FRAMES ###########
tabela = pd.read_csv("Rules.csv", sep=",")
df = pd.DataFrame(tabela)
df_new = (df.iloc[:, [4,25]])
df_id = (df.iloc[:, [24]])
df_identifier = pd.DataFrame()

_current = ''
for rule_name in rules:
    if rule_name != _current:
        row_number = df_new[df_new['rule.name'] == rule_name].index[0]
        rule_id = (df_id.iloc[[row_number]])
        df_identifier = pd.concat([df_identifier, rule_id], ignore_index=True)
id_list =(df_identifier['rule.identifier'].tolist())

def merge(id_list, rules):
    merged_list = [(id_list[i], rules[i]) for i in range(0, len(id_list))]
    return merged_list

merged_lists = (merge(id_list, rules))


########## TFA CREATION ##########
api_url = 'https://XXX.XXX.XXX.XXX/securitymanager/api/domain/DOMAIN/device/DEVICE/trafficflow'

cluster = 'CLUSTER_NAME' # Enter the cluster name
domainId = 'DOMAIN_ID' # Enter the Domain ID
deviceId = 'DEVICE_ID' # Enter the Device ID
duration = 'X' # Enter the Duration (1, 7 and 30)
create = 'DD-MM-YY' #Enter the Creation Date (DD-MM-YY)
endDate = 'YYYY-MM-DD' #Enter the End Date (YYYY-MM-DD)

for id, name in merged_lists:
    if id != _current:
        TFAName = (f'{cluster}-{name}-{create}') 
        data = {
            "domainId": domainId,
            "name": TFAName,
            "description": (f"Traffic flow para a regra: {name}"),
            "deviceId": deviceId,
            "ruleId": id,
            "duration": duration,
            "endDate": (f"{endDate}T00:00:00.000Z")
        }
        creation_response = requests.post (url=api_url, json=data, auth=('USER', 'PASSWORD'), verify=False)
        if creation_response.status_code >= 200 and creation_response.status_code <= 299:
            #Sucess
            print('Status Code:', creation_response.status_code)
            print('Reason:', creation_response.reason)
        else: 
            #Erro
            print('Status Code:', creation_response.status_code)
            print('Reason:', creation_response.reason)