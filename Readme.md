# Firemon TFA Creation By API

> The script consists of creating Traffic Flow Analysis (TFA) of the Firemon tool automatically via API based on the rules informed by the user.

## 💻 Prerequisites

Before you begin, make sure you have met the following requirements:

* You have installed the Pandas library `<pip install pandas>`
* You have installed the Requests library `<pip install requests>`
* You have installed the Urllib3 library `<pip install urllib3>`
* You have installed the Time library `<pip install time>`

## 🚀 Using the Firemon TFA Creation By API

To use the <Firemon TFA Creation By API>, follow these steps:

1. Enter the rules by which the tool will create TFAs in the “Rules.py” file:
2. Make a Firemon export .csv from the rule base present in Firemon and rename the file to "Rules.csv":
3. Start the script!
4. After starting the Script, you will need to enter the Username and Password to authenticate with Firemon.
5. The Script will ask for the name of the Firewall for which it will create the TFAs.
      The name must be without spaces.
6. Once the Cluster is informed, you will be asked for the Firemon IP, DomainID, DeviceID and TFAs Duration.
      The DomainID and DeviceID must be an integer.
      The Duration is only valid 1, 7 and 30 days.
   
Once these steps are done, the Script will create the TFAs based on the rules informed in the list in the “Rules.py” file, remembering that it is necessary to have a connection with your Firemon.

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
