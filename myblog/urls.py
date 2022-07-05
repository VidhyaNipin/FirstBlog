
from django.urls import path

from myblog import views

urlpatterns = [
    # path('home/', views.home, name='home'),
    path('index/', views.postlist, name='index'),
    # path('index', views.PostList.as_view(), name='index'),
    path('<slug:slug>/', views.PostDetails.as_view(), name='post_detail'),
]