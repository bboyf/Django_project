from django.core.management.base import BaseCommand
from polls.models import Subject, Teacher, User
from polls.utils import gen_md5_digest
from datetime import date


class Command(BaseCommand):
    help = '初始化数据库并添加示例数据'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('开始初始化数据库...'))
        
        # 清空现有数据
        self.stdout.write('清空旧数据...')
        Subject.objects.all().delete()
        Teacher.objects.all().delete()
        User.objects.filter(username='admin').delete()
        self.stdout.write(self.style.SUCCESS('✓ 旧数据已清空'))
        
        # 创建学科
        self.stdout.write('创建学科数据...')
        s1 = Subject.objects.create(name='Python全栈开发', intro='学习Python Web开发、数据分析等', is_hot=1)
        s2 = Subject.objects.create(name='Java企业级开发', intro='学习Java EE、Spring Boot等', is_hot=1)
        s3 = Subject.objects.create(name='前端开发', intro='学习HTML、CSS、JavaScript、Vue等', is_hot=1)
        s4 = Subject.objects.create(name='人工智能', intro='学习机器学习、深度学习等', is_hot=1)
        self.stdout.write(self.style.SUCCESS(f'  ✓ 已创建 4 个学科'))
        
        # 创建教师
        self.stdout.write('创建教师数据...')
        Teacher.objects.create(
            name='张三', sex=1, birth=date(1985, 3, 15),
            intro='10年Python开发经验', photo='teacher1.jpg',
            good_count=150, bad_count=5, subject=s1
        )
        Teacher.objects.create(
            name='李四', sex=1, birth=date(1982, 7, 20),
            intro='资深Java架构师', photo='teacher2.jpg',
            good_count=200, bad_count=8, subject=s2
        )
        Teacher.objects.create(
            name='王五', sex=0, birth=date(1990, 5, 10),
            intro='前端开发专家', photo='teacher3.jpg',
            good_count=180, bad_count=3, subject=s3
        )
        Teacher.objects.create(
            name='赵六', sex=1, birth=date(1988, 11, 25),
            intro='AI领域专家', photo='teacher4.jpg',
            good_count=220, bad_count=10, subject=s4
        )
        self.stdout.write(self.style.SUCCESS(f'  ✓ 已创建 4 位教师'))
        
        # 创建测试用户
        self.stdout.write('创建测试用户...')
        User.objects.create(
            username='admin',
            password=gen_md5_digest('123456'),
            tel='13800138000'
        )
        self.stdout.write(self.style.SUCCESS(f'  ✓ 已创建用户: admin (密码: 123456)'))
        
        self.stdout.write(self.style.SUCCESS('\n数据初始化完成！'))
        self.stdout.write('访问地址: http://localhost:8000/')
        self.stdout.write('登录账号: admin / 123456')

