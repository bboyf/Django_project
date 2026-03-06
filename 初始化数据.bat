@echo off
chcp 65001 >nul
cls
echo ========================================
echo  初始化数据库
echo ========================================
echo.

cd /d "%~dp0djangoproject"

echo [1/2] 执行数据库迁移...
..\vip4\Scripts\python.exe manage.py migrate
if errorlevel 1 (
    echo.
    echo 迁移失败！请检查:
    echo 1. MySQL服务是否启动
    echo 2. 数据库teacher_rating是否存在
    echo 3. 密码是否正确(settings.py第90行)
    pause
    exit /b 1
)

echo.
echo [2/2] 添加示例数据...
..\vip4\Scripts\python.exe manage.py setup_data
if errorlevel 1 (
    echo.
    echo 添加数据失败！
    pause
    exit /b 1
)

echo.
echo ========================================
echo ✓ 初始化完成！
echo ========================================
echo.
echo 现在可以运行: 启动.bat
pause
