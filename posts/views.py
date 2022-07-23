from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Post, Group, User, Comment, Book
from django.views.generic import FormView
from django.views.generic import CreateView
from .forms import PostForm, BookForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound

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
        form = PostForm(request.POST or None, files=request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
        else:
            return render(request, 'new.html', {'form': form})
    else:
        form = PostForm()
    return render(request, 'new.html',
                  {'form': form,
                   'button_name': 'Добавить',
                   'title': 'Добавить запись',
                   'url_name': 'new_post'}
                  )



class Test(CreateView):
    form_class = BookForm
    success_url = reverse_lazy("index") #  где login — это параметр "name" в path()
    template_name = "test.html"



def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = user.posts555.order_by('-pub_date').all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'name': user,
        'posts_count': user.posts555.count(),
        'author': request.user,
        "paginator": paginator,
        "page": page,
    }
    return render(request, 'profile.html', context=context)


def post_view(request, username, post_id):
    user = get_object_or_404(User, username=username)
    # post = user.posts555.get(id = post_id)
    post = get_object_or_404(Post, id=post_id, author_id=user.id)
    context = {
        'name': user,
        'post': post,
        'author': request.user,
        'posts_count': user.posts555.count(),
        'form': PostForm(),
        'items': Comment.objects.order_by('-created').filter(post_id=post_id),
    }
    return render(request, 'post.html', context=context)

@login_required()
def add_comment(request, username, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = Post.objects.get(id=post_id)
            comment.save()
            return redirect('post', username=username, post_id=post_id)
        else:
            return render(request, 'comments.html', {'form': form})
    else:
        form = CommentForm()
        return render(request, 'comments.html',
                      {'form': form,
                       'items': Comment.objects.order_by('created').filter(post_id=post_id),
                       'post': Post.objects.get(id=post_id)
                       }
                      )


@login_required()
def post_edit(request, username, post_id):
    # тут тело функции. Не забудьте проверить,
    # что текущий пользователь — это автор записи.
    # В качестве шаблона страницы редактирования укажите шаблон создания новой записи
    # который вы создали раньше (вы могли назвать шаблон иначе)
    user = get_object_or_404(User, username=username)
    post = get_object_or_404(Post, id=post_id, author_id = user.id)

    if username == request.user.username:
        if request.method == 'POST':
            form = PostForm(request.POST or None, files=request.FILES or None, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('profile', username=username)
        else:
            form = PostForm(instance=post)
        return render(request, 'new.html',
                      {'form': form,
                       'post_id': post_id,
                       'username': username,
                       'button_name': 'Сохранить',
                       'title': 'Редактировать запись',
                       'url_name': 'post_edit',}
                      )
    else:
        return redirect('post', username=username, post_id=post_id)


def page_not_found(request, exception):
    # Переменная exception содержит отладочную информацию,
    # выводить её в шаблон пользователской страницы 404 мы не станем
    return render(
        request,
        "misc/404.html",
        {"path": request.path},
        status=404
    )


def server_error(request):
    return render(request, "misc/500.html", status=500)




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

