# 🎓 Django 投票与教务管理系统

这是一个基于 Django 框架开发的 Web 应用，实现了用户登录注册、投票管理、学科与教师信息展示等功能。适合作为 Django 入门学习或课程设计参考。

## 🛠️ 技术栈
- **后端框架**: Django 4.x / 5.x
- **数据库**: SQLite (默认) / MySQL
- **前端技术**: HTML, CSS, JavaScript
- **验证码**: django-simple-captcha

## ✨ 功能模块
1.  **用户认证**: 注册、登录（含验证码）、注销。
2.  **投票系统**: 创建投票、参与投票、查看结果。
3.  **信息展示**: 学科列表、教师详情页。
4.  **后台管理**: 使用 Django Admin 管理所有数据。

## 🚀 快速开始

### 1. 环境准备
确保已安装 Python 3.8+。

```bash
# 克隆项目
git clone https://github.com/bboyf/Django_project.git
cd Django_project
```

### 2. 创建虚拟环境
建议使用虚拟环境隔离依赖：

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. 安装依赖
```bash
pip install django django-simple-captcha Pillow pymysql
# 或者如果有 requirements.txt
# pip install -r requirements.txt
```

### 4. 数据库迁移
```bash
cd djangoproject
python manage.py makemigrations
python manage.py migrate
```

### 5. 创建管理员账号
```bash
python manage.py createsuperuser
```

### 6. 启动项目
```bash
python manage.py runserver
```

打开浏览器访问 `http://127.0.0.1:8000/` 即可。

## 📂 目录结构
```
Django_project/
├── djangoproject/      # 项目根目录
│   ├── djangoproject/  # 核心配置 (settings, urls)
│   ├── polls/          # 投票应用 (views, models)
│   ├── static/         # 静态资源
│   ├── templates/      # HTML 模板
│   └── manage.py       # 管理脚本
└── README.md           # 项目文档
```