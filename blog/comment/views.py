from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from article.models import Article
from .models import Comment
from .forms import CommentForm

# Create your views here.

# 添加评论
@login_required(login_url='/login/')
def comment_post(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    # 处理POST请求
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.user = request.user
            new_comment.save()
            return redirect(article)
        else:
            return HttpResponse("表单内容有误， 请重新填写。")
    # 处理错误请求
    else:
        return HttpResponse("发表评论仅接受POST请求")

# 删除评论
def comment_delete(request, article_id, id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        comment = Comment.objects.get(id=id)
        comment.delete()
        return redirect(article)
    else:
        return HttpResponse("仅允许POST请求")



def comment_update(request):
    pass