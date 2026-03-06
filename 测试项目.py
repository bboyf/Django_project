#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""测试Django项目配置"""

import os
import sys

# 添加项目路径
project_dir = r'H:\Django项目\djangoproject'
sys.path.insert(0, project_dir)
os.chdir(project_dir)

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproject.settings')

print("=" * 60)
print("Django项目配置测试")
print("=" * 60)

# 测试Django导入
try:
    import django
    print(f"✓ Django版本: {django.get_version()}")
except ImportError as e:
    print(f"✗ Django导入失败: {e}")
    sys.exit(1)

# 初始化Django
try:
    django.setup()
    print("✓ Django初始化成功")
except Exception as e:
    print(f"✗ Django初始化失败: {e}")
    sys.exit(1)

# 测试数据库连接
try:
    from django.db import connection
    connection.ensure_connection()
    print("✓ MySQL数据库连接成功")
except Exception as e:
    print(f"✗ 数据库连接失败: {e}")
    print("\n请检查:")
    print("1. MySQL服务是否启动")
    print("2. 数据库teacher_rating是否存在")
    print("3. settings.py中的密码是否正确")
    sys.exit(1)

# 检查模型
try:
    from polls.models import Subject, Teacher, User
    print("✓ 模型导入成功")
except Exception as e:
    print(f"✗ 模型导入失败: {e}")
    sys.exit(1)

# 检查数据
try:
    subject_count = Subject.objects.count()
    teacher_count = Teacher.objects.count()
    user_count = User.objects.count()
    print(f"✓ 数据统计: 学科{subject_count}个, 教师{teacher_count}位, 用户{user_count}个")
except Exception as e:
    print(f"⚠ 数据查询失败: {e}")
    print("   可能需要运行: 初始化数据.bat")

print("\n" + "=" * 60)
print("配置测试完成！")
print("=" * 60)
print("\n如果所有检查都通过，可以运行: 启动.bat")

