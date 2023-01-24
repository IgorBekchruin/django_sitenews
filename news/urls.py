from django.urls import path
from .views import HomeView,  PostDetailView, PostList, PostByCategory, PopularPostList


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('posts', PostList.as_view(), name='post_list'),
    path('popular_post', PopularPostList.as_view(), name='popular_post_list'),
    path('post/<slug:slug>', PostDetailView.as_view(), name='post_detail'),
    path('post/category/<slug:slug>/', PostByCategory.as_view(), name='postbycategory')
]