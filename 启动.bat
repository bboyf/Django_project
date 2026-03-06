@echo off
cd /d "%~dp0djangoproject"
echo 启动Django服务器...
echo.
echo 访问地址: http://localhost:8000/
echo 登录账号: admin / 123456
echo.
..\vip4\Scripts\python.exe manage.py runserver

