from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts555")
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING, blank=True,
                              null=True, related_name="posts555")
    image = models.ImageField(upload_to='posts/', blank=True, null=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField(
        max_length=1000,
        verbose_name='Комментарий к посту',
        help_text='Добавьте комментарий к посту'
    )
    created = models.DateTimeField("date created", auto_now_add=True)

    def __str__(self):
        return self.text


class Book(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author1 = models.CharField(max_length=20)

    def __str__(self):
        return self.text


# class New(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     slug = models.SlugField(unique=True)
#
#     def __str__(self):
#         return self.title


# from django.db import models
# from django.contrib.auth import get_user_model
#
# User = get_user_model()
#
#
# class Event(models.Model):
#     name = models.TextField(max_length=200)
#     start_at = models.DateTimeField("date published", auto_now_add=True)
#     description = models.TextField()
#     contact = models.EmailField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
#     location = models.TextField(max_length=400)
