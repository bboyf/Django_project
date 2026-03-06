Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = "H:\Django项目"
WshShell.Run "cmd /k 一键启动.bat", 1

