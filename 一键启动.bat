@echo off
chcp 65001 >nul
cls
echo.
echo ========================================
echo   Django教师评价系统 - 一键启动
echo ========================================
echo.
echo 正在检查环境...
echo.

cd /d "%~dp0djangoproject"

echo [1/3] 检查数据库连接...
..\vip4\Scripts\python.exe -c "import django, os; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproject.settings'); django.setup(); from django.db import connection; connection.ensure_connection(); print('数据库连接成功')"
if errorlevel 1 (
    echo.
    echo ✗ 数据库连接失败！
    echo.
    echo 请确保：
    echo 1. MySQL服务已启动
    echo 2. 数据库 teacher_rating 已创建
    echo 3. 密码正确 (settings.py 第90行)
    echo.
    pause
    exit /b 1
)

echo.
echo [2/3] 检查数据库表...
..\vip4\Scripts\python.exe manage.py migrate --check >nul 2>&1
if errorlevel 1 (
    echo.
    echo ⚠ 数据库未初始化，正在初始化...
    ..\vip4\Scripts\python.exe manage.py migrate
    if errorlevel 1 (
        echo.
        echo ✗ 数据库初始化失败！
        pause
        exit /b 1
    )
    echo.
    echo [*] 添加示例数据...
    ..\vip4\Scripts\python.exe manage.py setup_data
)

echo.
echo [3/3] 启动服务器...
echo.
echo ========================================
echo  服务器信息
echo ========================================
echo  访问地址: http://localhost:8000/
echo  登录账号: admin / 123456
echo.
echo  按 Ctrl+C 可停止服务器
echo ========================================
echo.

..\vip4\Scripts\python.exe manage.py runserver

pause

