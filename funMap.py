# $language = "python"
# $interface = "1.0"

ftpUser = "1"
ftpPwd = "1"

def execCMD(cmd, expectRes, timeout=3):
    crt.Screen.Send(cmd + '\r')
    res =  crt.Screen.WaitForStrings([expectRes], timeout)
    if res == 0:
        raise ScriptError(cmd)

def LoginFtp(ftpUser='1', ftpPwd='1', ip=crt.Session.LocalAddress):
    crt.Screen.Synchronous = True
    try:
        execCMD('ftp '+ip, 'user')
        execCMD(ftpUser, 'password')
        execCMD(ftpPwd, 'ftp')
        execCMD('bin', 'ftp')
    except:
        #crt.Dialog.MessageBox("Login Fail!")
        pass
    crt.Screen.Synchronous = False

def FtpPut():
    crt.Screen.Send('ftpput -u ' +ftpUser+ ' -p ' +ftpPwd+ ' ' + crt.Session.LocalAddress + ' ')

def FtpGet():
    crt.Screen.Send('ftpget -u ' +ftpUser+ ' -p ' +ftpPwd+ ' ' + crt.Session.LocalAddress + ' ')

inputstr = crt.Arguments[0]

funMap = {'loginftp':LoginFtp,
'ftpput':FtpPut,
'ftpget':FtpGet
}

if inputstr in funMap:
    funMap[inputstr]()
else:
    crt.Dialog.MessageBox("没有该参数的函数!")
