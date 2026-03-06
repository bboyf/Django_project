from urllib import request
from django.shortcuts import render, redirect
from polls.models import Subject, Teacher
from django.http import HttpRequest, HttpResponse

def show_subjects(request):
    subjects = Subject.objects.all().order_by('no')
    return render(request, 'polls/subjects.html', {'subjects': subjects})
# 会默认找到templates文件下的对应html文件。
def show_teachers(request):
    try:
        sno = int(request.GET.get('sno'))
        teachers = []
        if sno:
            subject = Subject.objects.only('name').get(no=sno)
            teachers = Teacher.objects.filter(subject=subject).order_by('no')
        return render(request, 'polls/teachers.html', {
            'subject': subject,
            'teachers': teachers
        })
    except (ValueError, Subject.DoesNotExist):
        return redirect('/')
from django.http import JsonResponse

def praise_or_criticize(request: HttpRequest) -> HttpResponse:
    if request.session.get('userid'):
        try:
            tno = int(request.GET.get('tno'))
            teacher = Teacher.objects.get(no=tno)
            if request.path.startswith('/praise/'):
                teacher.good_count += 1
                count = teacher.good_count
            else:
                teacher.bad_count += 1
                count = teacher.bad_count
            teacher.save()
            data = {'code': 20000, 'mesg': '投票成功', 'count': count}
        except (ValueError, Teacher.DoesNotExist):
            data = {'code': 20001, 'mesg': '投票失败'}
    else:
        data = {'code': 20002, 'mesg': '请先登录'}
    return JsonResponse(data)









# def praise_or_criticize(request):
#     """好评"""
#     try:
#         tno = int(request.GET.get('tno'))
#         teacher = Teacher.objects.get(no=tno)
#         if request.path.startswith('/praise'):
#             teacher.good_count += 1
#             count = teacher.good_count
#         else:
#             teacher.bad_count += 1
#             count = teacher.bad_count
#         teacher.save()
#         data = {'code': 20000, 'mesg': '操作成功', 'count': count}
#     except (ValueError, Teacher.DoseNotExist):
#         data = {'code': 20001, 'mesg': '操作失败'}
#     return JsonResponse(data)





from polls.Captcha import Captcha
from polls.utils import gen_md5_digest, gen_random_code

from polls.models import User
# 编写用户登录的视图函数和模板页
def login(request: HttpRequest) -> HttpResponse:
    hint = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        captcha = request.POST.get('captcha')
        
        # 验证验证码
        session_captcha = request.session.get('captcha', '')
        if not captcha:
            hint = '请输入验证码'
        elif captcha.upper() != session_captcha.upper():
            hint = '验证码错误'
            # 清除session中的验证码，防止重复使用
            request.session.pop('captcha', None)
        elif not username or not password:
            hint = '请输入有效的用户名和密码'
        else:
            # 清除验证码
            request.session.pop('captcha', None)
            # 验证用户名和密码
            password = gen_md5_digest(password)
            user = User.objects.filter(username=username, password=password).first()
            if user:
                request.session['userid'] = user.no
                request.session['username'] = user.username
                return redirect('/')
            else:
                hint = '用户名或密码错误'
    return render(request, 'login.html', {'hint': hint})



from polls.Captcha import Captcha
from polls.utils import gen_random_code



def get_captcha(request: HttpRequest) -> HttpResponse:
    """验证码"""
    captcha_text = gen_random_code()
    request.session['captcha'] = captcha_text
    image_data = Captcha.instance().generate(captcha_text)
    return HttpResponse(image_data, content_type='image/png')


# 如果用户没有登录，页面会显示登录和注册的超链接
def logout(request):
    """注销"""
    request.session.flush()
    return redirect('/')



def register(request: HttpRequest) -> HttpResponse:
    from datetime import datetime
    reg_date = datetime.now()

    hint = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password = gen_md5_digest(password)
        tel = request.POST.get('tel')
        user = User.objects.filter(username=username).first()
        if user:
            hint = '用户名已存在'
            return render(request, 'register.html', {'hint': hint})

        print(reg_date,"<--------reg_date")
        user = User(username=username,password=password,tel=tel,reg_date=reg_date,)
        user.save()

        
        user = User.objects.filter(username=username).first()
        if user:
            hint="用户 {} 注册成功".format(username)
            return redirect('/')
        else:
            hint = '请重新注册'
            return render(request, 'register.html', {'hint': hint})

    return render(request, 'register.html', {'hint': hint})
