"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import imp
# import sys,os
# sys.path.append(os.path.dirname(__file__) + os.sep + '../')
from django.contrib import admin
from django.urls import path
from polls import views as polls_views

urlpatterns = [
    # 管理后台
    path("admin/", admin.site.urls),
    
    # 主页和学科展示
    path('', polls_views.show_subjects, name='home'),
    
    # 教师相关
    path('teachers/', polls_views.show_teachers, name='teachers'),
    path('praise/', polls_views.praise_or_criticize, name='praise'),
    path('criticize/', polls_views.praise_or_criticize, name='criticize'),
    
    # 用户认证
    path('login/', polls_views.login, name='login'),
    path('logout/', polls_views.logout, name='logout'),
    path('register/', polls_views.register, name='register'),
    path('captcha/', polls_views.get_captcha, name='captcha'),
]
