from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("plans/", views.my_index, name="index2"),
    path("group/<slug:slug>/", views.group_posts, name="group")
]