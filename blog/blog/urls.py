"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path

import article.views
import user.views
import comment.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', article.views.hello),
    #re_path(r'^$', views.article_list),
    path('article/list/', article.views.article_list, name='list'),
    path('article/detail/<int:id>/', article.views.article_detail, name='detail'),
    path('article/create/', article.views.article_create, name='create'),
    path('article/delete/<int:id>/', article.views.article_delete, name='delete'),
    path('article/update/<int:id>/', article.views.article_update, name='update'),
    path('user/login/', user.views.user_login, name='login'),
    path('user/logout/', user.views.user_logout, name='logout'),
    path('user/register/', user.views.user_register, name='register'),
    path('comment/post/<int:article_id>/', comment.views.comment_post, name='comment_post'),
    path('comment/delete/<int:article_id>/<int:id>/', comment.views.comment_delete, name='comment_delete'),
]
