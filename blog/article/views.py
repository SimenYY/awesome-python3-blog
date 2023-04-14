from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Article
# 引入redirect用于重定向地址
from django.shortcuts import render, redirect
from .forms import ArticleForm
from comment.models import Comment
from django.urls import reverse


def hello(request):
    return HttpResponse("Hello world! ")

def article_list(request):
    # 取出所有博客文章
    articles = Article.objects.all()
    # 需要传递给模板（templates）的对象
    context = { 'articles':articles}
    # render函数：载入模板，并返回context对象
    return render(request, 'article/list.html', context)

def article_detail(request, id):
    # 取出相应的文章
    article = Article.objects.get(id=id)
    # 取出文章的评论
    comments = Comment.objects.filter(article=id)
    # 需要传递给模板的对象
    context = {'article':article, 'comments':comments}
    # 载入模板，并返回context对象
    return render(request, 'article/detail.html', context)

# 写文章的视图
def article_create(request):
    # 判断用户是否提交数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticleForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_article = article_post_form.save(commit=False)
            # 作者为当前请求的用户名
            new_article.author = request.user
            # 将新文章保存到数据库中
            new_article.save()
            # 完成后返回到文章列表
            return redirect("list")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticleForm()
        # 赋值上下文
        context = { 'article_post_form': article_post_form }
        # 返回模板
        return render(request, 'article/create.html', context)

#删除文章
def article_delete(request, id):
    if request.method == 'POST':
        article = Article.objects.get(id=id)
        article.delete()
        return  redirect("list")
    else:
        return HttpResponse("仅允许POST请求")

# 更新文章
def article_update(request, id):
    """
    更新文章的视图函数
    通过POST方法提交表单，更新titile、body字段
    GET方法进入初始表单页面
    id： 文章的 id
    """

    # 获取需要修改的具体文章对象
    article = Article.objects.get(id=id)
    # 判断用户是否为 POST 提交表单数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticleForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存新写入的 title、body 数据并保存
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            # 完成后返回到修改后的文章中。需传入文章的 id 值
            # return redirect(reverse("article:article_detail"), id=id)
            return redirect(article)
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")

    # 如果用户 GET 请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticleForm()
        # 赋值上下文，将 article 文章对象也传递进去，以便提取旧的内容
        context = { 'article': article, 'article_post_form': article_post_form }
        # 将响应返回到模板中
        return render(request, 'article/update.html', context)
