from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Post, Group, User

import datetime as dt


def index(request):
    # latest = Post.objects.order_by('-pub_date')[:11]
    # return render(request, "index.html", {"posts": latest})
    #
    # author = User.objects.get(last_name = 'Толстой')
    # keyword = "утро"
    # start_date = dt.date(1854, 7, 7)
    # end_date = dt.date(1854, 7, 21)
    # range1 = (start_date, end_date)
    # # posts = Post.objects.filter(author=author, pub_date__range=range1, text__contains=keyword).order_by(
    # #     '-pub_date')
    # return render(request, "index2.html", {"posts": posts})

    keyword = request.GET.get("q", None)

    if keyword:
        posts = Post.objects.select_related(
            'author', 'group'
        ).filter(text__contains=keyword)
    else:
        posts = None

    return render(request, "index2.html", {"posts": posts, "keyword": keyword})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts555.all()[:12]
    return render(request, "group.html", {"group": group, "posts": posts})

# def my_index(request):
#     plans = [
#         {
#             "name": "Бесплатно",
#             "price": "0",
#             "options": {"users": 10, "space": 10, "support": "Почтовая рассылка"},
#         },
#         {
#             "name": "Профессиональный",
#             "price": "49",
#             "options": {"users": 50, "space": 100, "support": "Телефон и email"},
#         },
#         {
#             "name": "Корпоративный",
#             "price": "99",
#             "options": {"users": 100, "space": 500, "support": "Персональный менеджер"},
#         },
#     ]
#     data = {'plans' : plans}
#     return render(
#         request,  # первый параметр — это всегда request
#         'index.html',  # имя шаблона, который нужен для отображения страницы
#         context=data
#         # {'plans': 'Этот текст встанет в шаблон на место переменной "title"'}
#         # словарь содержит переменные, которые будут переданы в шаблон
#     )
