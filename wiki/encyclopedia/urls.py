from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("page/<str:name>" , views.page , name="page"),
    path("search/<str:query>" , views.search , name="search"),
    path("new_page" , views.new_page , name="new_page"),
    path("random/" , views.rand , name="random")
]
