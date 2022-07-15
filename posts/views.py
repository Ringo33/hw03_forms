from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Post, Group, User, Book
from django.views.generic import FormView
from django.views.generic import CreateView
from .forms import PostForm, BookForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.urls import reverse_lazy
from django.core.paginator import Paginator

import datetime as dt


def index(request):
    post_list = Post.objects.order_by('-pub_date').all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(
        request,
        "index.html",
        {"page": page, "paginator": paginator}
    )


    # author = User.objects.get(last_name = 'Толстой')
    # keyword = "утро"
    # start_date = dt.date(1854, 7, 7)
    # end_date = dt.date(1854, 7, 21)
    # range1 = (start_date, end_date)
    # # posts = Post.objects.filter(author=author, pub_date__range=range1, text__contains=keyword).order_by(
    # #     '-pub_date')
    # return render(request, "index2.html", {"posts": posts})

    # keyword = request.GET.get("q", None)
    # if keyword:
    #     posts = Post.objects.select_related(
    #         'author', 'group'
    #     ).filter(text__contains=keyword)
    # else:
    #     posts = None
    # return render(request, "index2.html", {"posts": posts, "keyword": keyword})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts555.order_by('pub_date').all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(
        request, "group.html",
        {"page": page,
        "group": group,
        "paginator": paginator}
    )


@login_required()
def new_post(request):
    """Добавить новую запись, если пользователь зарегистрирован"""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
        else:
            return render(request, 'new.html', {'form': form})
    else:
        form = PostForm()
    return render(request, 'new.html', {'form': form})



class Test(CreateView):
    form_class = BookForm
    success_url = reverse_lazy("index") #  где login — это параметр "name" в path()
    template_name = "test.html"



def profile(request, username):
    user = get_object_or_404(User, username=username)


    return render(request, 'profile.html', {})


def post_view(request, username, post_id):
    # тут тело функции
    return render(request, 'post.html', {})


def post_edit(request, username, post_id):
    # тут тело функции. Не забудьте проверить,
    # что текущий пользователь — это автор записи.
    # В качестве шаблона страницы редактирования укажите шаблон создания новой записи
    # который вы создали раньше (вы могли назвать шаблон иначе)
    return render(request, 'post_new.html', {})




# class PostForm(FormView):
#     form_class = PostForm
#     success_url = reverse_lazy("index") #  где login — это параметр "name" в path()
#     template_name = "new.html"
#
#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         group = form.cleaned_data['group']
#         text = form.cleaned_data['text']
#
#
#         Post.objects.create(text=text, group_id=Group.objects.get(title=group).id, author_id=User.objects.get(username='admin').id)
#
#         return super().form_valid(form)

