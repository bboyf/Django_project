========================================
        教师评价系统
========================================

【快速开始】推荐方式
--------------

方式1: 一键启动（推荐）
双击运行: 一键启动.bat
  - 自动检查数据库连接
  - 自动初始化数据库（如果需要）
  - 自动启动服务器

方式2: 手动步骤
步骤1: 创建MySQL数据库
  在CMD中执行:
  mysql -u root -pzhangxin123 -e "CREATE DATABASE teacher_rating DEFAULT CHARACTER SET utf8mb4"

步骤2: 初始化数据
  双击运行: 初始化数据.bat

步骤3: 启动服务器
  双击运行: 启动.bat

访问: http://localhost:8000/
登录: admin / 123456


【MySQL配置】
------------
主机: localhost
端口: 3306
用户: root
密码: zhangxin123
数据库: teacher_rating

如果密码不同，修改:
djangoproject\djangoproject\settings.py (第90行)


【常见问题】
----------

Q: 初始化失败？
A: 1. 确保MySQL服务已启动
   2. 确保已创建teacher_rating数据库
   3. 检查settings.py中的密码

Q: 页面打不开？
A: 1. 确保看到 "Starting development server"
   2. 尝试访问 http://127.0.0.1:8000/

Q: 页面显示错误？
A: 1. 确保已运行 初始化数据.bat
   2. 查看命令行窗口的错误信息


【项目结构】
----------
djangoproject\       - Django项目
  polls\             - 主应用
  templates\         - HTML模板
  static\            - 静态文件
vip4\                - Python虚拟环境
初始化数据.bat       - 首次运行执行
启动.bat             - 启动Django服务器
测试项目.py          - 测试工具
简易说明.txt         - 快速参考


========================================
