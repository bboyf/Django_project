@echo off
chcp 65001 >nul
cd /d "%~dp0djangoproject"
echo ========================================
echo  启动Django服务器
echo ========================================
echo.
echo 访问地址: http://localhost:8000/
echo 登录账号: admin / 123456
echo.
echo 按 Ctrl+C 停止服务器
echo ========================================
echo.
..\vip4\Scripts\python.exe manage.py runserver
pause

