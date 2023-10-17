# rdp2ngrok
Automatically setup RDP with ngrok

## Installation
```
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-Expression "& { $(Invoke-WebRequest -UseBasicParsing 'https://raw.githubusercontent.com/carince/rdp2ngrok/main/install.ps1') }"
```