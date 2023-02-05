function getIP {
(get-netipaddress).ipv4address |Select-String "192*"
}
$IP = getIP
$USER = whoami
$PS = $HOST.Version.Major


Write-Host("This is this machine's IP: $IP")
$BODY = ("This machine's IP is $IP . The user is $USER . Hostname is $HOSTNAME . Powershell version is $PS .")

Send-MailMessage -To "leonardf@ucmail.uc.edu" -From "juhasjon9@gmail.com" -Subject "IT3038c Windows SysInfo" -Body $BODY -SmtpServer smpt.gmail.com -port 587 -UseSSL -Credential (Get-Credential)
