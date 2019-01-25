# $language = "python"
# $interface = "1.0"


data = {}

with open("env_info.csv") as f:
    filelines = f.readlines()

for fileline in filelines:
    fileline = fileline.split(',')
    data[fileline[4]] = fileline[5]

if crt.Session.RemoteAddress in data:
    userpwd = data[crt.Session.RemoteAddress].split('/')
    crt.Screen.Send(userpwd[0] + '\r')
    crt.Screen.WaitForStrings('Password', 3)
    crt.Screen.Send(userpwd[1] + '\r')
    res = crt.Screen.WaitForStrings(['<', 'Y/N'], 3)
    if res == 2:
        crt.Screen.Send('n\r')
    #crt.Dialog.MessageBox(str(data[crt.Session.RemoteAddress]))
else:
    crt.Dialog.MessageBox("无记录！")
