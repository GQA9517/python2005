from django.core.paginator import Paginator
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.urls import reverse

from course.models import Category, Article


# 首页
def index(request):
    # 接收页号
    number = request.GET.get('number', 1)
    # 查询所有的一级分类
    cate_list = Category.objects.filter(level=1)
    # 查询所有的二级分类
    sub_cate_list = Category.objects.filter(level=2)
    # 查询所有的文章
    art_list = Article.objects.all()
    # 分页器对象
    paginator = Paginator(object_list=art_list, per_page=3)
    page = paginator.page(number)
    return render(request, 'course/index.html',
                  {'cate_list': cate_list, 'sub_cate_list': sub_cate_list, 'page': page})


# 文章列表页面
def article_list(request):
    # 接收页号
    number = request.GET.get('number', 1)
    # 查询所有的一级分类
    cate_list = Category.objects.filter(level=1)
    # 查询所有的二级分类
    sub_cate_list = Category.objects.filter(level=2)
    # 获取当前点击的是一级分类还是二级分类
    level = request.GET.get('level')
    # 获取当前点击的分类的id (一级或二级)
    id = request.GET.get('id')
    art_list = None
    parent = None

    if level == '1':
        art_list = Article.objects.filter(cate__parent_id=id)
    else:
        art_list = Article.objects.filter(cate__id=id)
        parent = Category.objects.get(pk=Category.objects.get(pk=id).parent_id)
    # 分页器对象
    paginator = Paginator(object_list=art_list, per_page=3)
    page = paginator.page(number)
    return render(request, 'course/article_list.html', {
        'cate_list': cate_list,
        'sub_cate_list': sub_cate_list,
        'page': page,
        'level': level,
        'id': id,
        'title': Category.objects.get(pk=id).title,
        'parent': parent
    })


# 增加课程/分类
def add_course(request):
    # 查询所有的一级分类
    cate_list = Category.objects.filter(level=1)
    # 查询所有的二级分类
    sub_cate_list = Category.objects.filter(level=2)
    return render(request, 'course/addCourse.html', {
        'cate_list': cate_list,
        'sub_cate_list': sub_cate_list,
    })


def add_course_logic(request):
    title = request.POST.get('title')
    level = request.POST.get('level')
    if level == '1':
        Category.objects.create(title=title, level=1)
    else:
        cate_id = request.POST.get('cate_sel')
        Category.objects.create(title=title, level=2, parent_id=cate_id)
    return redirect('/')

# 增加课文章
def add_article(request):
    # 查询所有的一级分类
    cate_list = Category.objects.filter(level=1)
    # 查询所有的二级分类
    sub_cate_list = Category.objects.filter(level=2)
    return render(request, 'course/addArticle.html', {
        'cate_list': cate_list,
        'sub_cate_list': sub_cate_list,
    })


def add_article_logic(request):
    title = request.POST.get('title')
    cate_sel = request.POST.get('cate_sel')
    publish_time = request.POST.get('publish_time')
    contents = request.POST.get('contents')
    Article.objects.create(title=title, publish_time=publish_time, page_views=0, contents=contents, cate_id=cate_sel)
    url = reverse('course:article_list') + '?level=2&id=' + cate_sel
    return redirect(url)


# 更新文章页面
def update_article(request):
    # 文章的id
    id = request.GET.get('id')
    art = Article.objects.get(id=id)
    # 查询所有的一级分类
    cate_list = Category.objects.filter(level=1)
    # 查询所有的二级分类
    sub_cate_list = Category.objects.filter(level=2)

    # 获取当前文章所属的课程下（一级分类）的所有的二级分类
    special_cate_list = Category.objects.filter(parent_id=art.cate.parent_id)
    return render(request, 'course/update.html', {
        'cate_list': cate_list,
        'sub_cate_list': sub_cate_list,
        'art': art,
        'special_cate_list': special_cate_list
    })


def update_article_logic(request):
    id = request.POST.get('id')
    title = request.POST.get('title')
    cate_sel = request.POST.get('cate_sel')
    contents = request.POST.get('contents')
    art = Article.objects.get(pk=id)
    art.title = title
    art.contents = contents
    art.cate_id = cate_sel
    art.save()
    url = reverse('course:article_list') + '?level=2&id=' + cate_sel
    return redirect(url)

"""


"""
# 删除文章
def delete_article(request):
    id = request.GET.get('id')
    fm = request.GET.get('from')
    level = request.GET.get('level')
    cate_id = request.GET.get('cate_id')
    Article.objects.get(pk=id).delete()
    to_url = fm+'?level='+level+'&id='+cate_id
    return redirect(to_url)


def get_sub_categories(request):
    # 一级分类id
    id = request.GET.get('id')
    cate_list = Category.objects.filter(parent_id=id)
    return JsonResponse({
        'cate_list': list(cate_list)},
        json_dumps_params={
            'default': lambda c: {
                'id': c.id,
                'title': c.title
            } if isinstance(c,Category) else None
        })


def test():
    print(111)
    print(222)
    return HttpResponse('测试')

