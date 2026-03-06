#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Django项目启动脚本"""

import os
import sys
import subprocess

# 项目路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.join(BASE_DIR, 'djangoproject')
PYTHON_EXE = os.path.join(BASE_DIR, 'vip4', 'Scripts', 'python.exe')

print("=" * 60)
print("   Django教师评价系统 - 启动")
print("=" * 60)
print()

# 切换到项目目录
os.chdir(PROJECT_DIR)
print(f"工作目录: {os.getcwd()}")
print()

# 设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproject.settings')

print("[1/3] 检查Django环境...")
try:
    import django
    print(f"[OK] Django {django.get_version()}")
    django.setup()
except Exception as e:
    print(f"[ERROR] Django初始化失败: {e}")
    sys.exit(1)

print()
print("[2/3] 检查数据库...")
try:
    from django.db import connection
    connection.ensure_connection()
    print("[OK] 数据库连接成功")
    
    # 检查是否需要迁移
    from django.core.management import execute_from_command_line
    from io import StringIO
    import contextlib
    
    # 检查迁移状态
    with contextlib.redirect_stdout(StringIO()):
        try:
            execute_from_command_line(['manage.py', 'migrate', '--check'])
            print("[OK] 数据库已初始化")
        except SystemExit as e:
            if e.code != 0:
                print("[INFO] 需要初始化数据库")
                print("  正在执行数据库迁移...")
                execute_from_command_line(['manage.py', 'migrate'])
                print("  正在添加示例数据...")
                try:
                    execute_from_command_line(['manage.py', 'setup_data'])
                except:
                    pass
                print("[OK] 数据库初始化完成")
except Exception as e:
    print(f"[ERROR] 数据库错误: {e}")
    print()
    print("请检查:")
    print("1. MySQL服务是否启动")
    print("2. 数据库 teacher_rating 是否存在")
    print("3. settings.py 中的密码是否正确")
    input("\n按回车键退出...")
    sys.exit(1)

print()
print("[3/3] 启动开发服务器...")
print()
print("=" * 60)
print("  访问地址: http://localhost:8000/")
print("  登录账号: admin / 123456")
print()
print("  按 Ctrl+C 可停止服务器")
print("=" * 60)
print()

# 启动服务器
subprocess.run([PYTHON_EXE, 'manage.py', 'runserver'])

input("\n按回车键退出...")
