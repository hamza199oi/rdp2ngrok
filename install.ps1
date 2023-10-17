Write-Host "rdp2ngrok by carince"
# Check for admin
if (!([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "rdp2ngrok must be ran as administrator."
}

# Download Python
Write-Host
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
Write-Host "Downloading python..."
Start-BitsTransfer -Source "https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe" -Destination "python-installer.exe"

# Install Python
Write-Host
Write-Host "Installing python..."
Start-Process -FilePath .\python-installer.exe -ArgumentList "/passive InstallAllUsers=0 InstallLauncherAllUsers=0 PrependPath=1 Include_test=0"
Start-Sleep -Seconds 5
Write-Host "Refreshing PATH"
$env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")

# Download script
dir = "C:\Program Files\Python312"
Set-Location $dir
Write-Host "Downloading script..."
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/carince/rdp2ngrok/master/app.py" -OutFile "app.py"
python -m pip install ngrok requests

Read-Host -Prompt "Press Enter to exit"