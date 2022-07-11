from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("plans/", views.my_index, name="index2"),
    path("group/<slug:slug>/", views.group_posts, name="group"),
    path("new/", views.new_post, name="new_post"),
    path("test/", views.Test.as_view(), name="test")
    # path("new/", views.PostForm.as_view(), name="new_post")
]