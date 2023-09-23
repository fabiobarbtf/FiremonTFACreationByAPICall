# Firemon TFA Creation By API

> The script consists of creating Traffic Flow Analysis (TFA) of the Firemon tool automatically via API based on the rules informed by the user.

## 💻 Prerequisites

Before you begin, make sure you have met the following requirements:

* You have installed the Pandas library `<pip install pandas>`
* You have installed the Requests library `<pip install requests>`
## 🚀 Using the <Firemon TFA Creation By API>

To use the <Firemon TFA Creation By API>, follow these steps:

Enter your Firemon's address in the variable "api_url" (line 29):
```
<api_url = 'https://XXX.XXX.XXX.XXX/securitymanager/api/domain/DOMAIN/device/DEVICE/trafficflow'>
```

Enter the dependencies in the variables below to fill in the API body (lines 31 to 35):
```
<cluster = 'CLUSTER_NAME' 
domainId = 'DOMAIN_ID' 
deviceId = 'DEVICE_ID' 
duration = 'X' 
create = 'DD-MM-YY' 
endDate = 'YYYY-MM-DD' 
```

Inform the rules by which the tool creates TFAs in the list present in the file "Rules.py" (line 5):
```
<rules = ['RULE', 'RULE', 'RULE', 'RULE']>
```

Remove a Firemon export .csv from the rule base present in Firemon and rename the file to "Rules.csv":
```
"Rules.csv"
```
Once this is done, simply run the script to generate the TFAs based on the rules informed in the list in the "Rules.py" file, remembering that you must have a connection to your Firemon.

## 🤝 Creator

To people who contributed and created this project:

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/144133682" width="100px;" alt="Photo by Fábio Barbosa on GitHub"/><br>
        <sub>
          <b>Fábio Barbosa</b>
        </sub>
      </a>
    </td>
  </tr>
</table>