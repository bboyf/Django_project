#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

# 切换目录
os.chdir(r'H:\Django项目\djangoproject')
print("当前目录:", os.getcwd())

# 设置Python路径
sys.path.insert(0, r'H:\Django项目\djangoproject')

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproject.settings')

print("=" * 60)
print("测试Django配置")
print("=" * 60)

# 测试Django导入
try:
    import django
    print(f"✓ Django版本: {django.get_version()}")
    django.setup()
    print("✓ Django初始化成功")
except Exception as e:
    print(f"✗ Django初始化失败: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# 测试数据库连接
try:
    from django.db import connection
    connection.ensure_connection()
    print("✓ 数据库连接成功")
except Exception as e:
    print(f"✗ 数据库连接失败: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# 测试验证码模块
try:
    from polls.Captcha import Captcha
    print("✓ 验证码模块导入成功")
    
    # 尝试生成验证码
    captcha = Captcha.instance()
    image_data = captcha.generate('TEST')
    print(f"✓ 验证码生成成功 (大小: {len(image_data)} bytes)")
except Exception as e:
    print(f"✗ 验证码测试失败: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)
print("测试完成！可以启动服务器")
print("=" * 60)

# 启动服务器
print("\n正在启动Django开发服务器...")
os.system(r'H:\Django项目\vip4\Scripts\python.exe manage.py runserver')

