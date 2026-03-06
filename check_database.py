#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""检查数据库内容"""

import os
import sys
import django

# 设置Django环境
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.join(BASE_DIR, 'djangoproject')
sys.path.insert(0, PROJECT_DIR)
os.chdir(PROJECT_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproject.settings')
django.setup()

from polls.models import Subject, Teacher, User

print("=" * 60)
print("数据库内容检查")
print("=" * 60)

# 检查用户
print("\n【用户数据】")
users = User.objects.all()
print(f"总数: {users.count()} 个用户")
for user in users:
    print(f"  - {user.username} (ID: {user.no})")

# 检查学科
print("\n【学科数据】")
subjects = Subject.objects.all()
print(f"总数: {subjects.count()} 个学科")
for subject in subjects:
    hot = "[热门]" if subject.is_hot else ""
    print(f"  {subject.no}. {subject.name} {hot}")

# 检查教师
print("\n【教师数据】")
teachers = Teacher.objects.all()
print(f"总数: {teachers.count()} 个教师")
for teacher in teachers:
    print(f"  - {teacher.name} ({teacher.subject.name}) - 好评:{teacher.good_count} 差评:{teacher.bad_count}")

print("\n" + "=" * 60)
print("检查完成")
print("=" * 60)

