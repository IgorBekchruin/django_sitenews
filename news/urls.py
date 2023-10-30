from django.urls import path
from django.views.decorators.cache import cache_page

from .views import (
    HomeView,
    PopularPostList,
    PostByCategory,
    PostByTagListView,
    PostDetailView,
    PostList,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("posts", cache_page(60 * 2)(PostList.as_view()), name="post_list"),
    path("popular_post", cache_page(60 * 2)(PopularPostList.as_view()), name="popular_post_list"),
    path("post/<slug:slug>", PostDetailView.as_view(), name="post_detail"),
    path("post/tags/<str:tag>/", cache_page(60 * 5)(PostByTagListView.as_view()), name="post_by_tags"),
    path("post/category/<slug:slug>/", PostByCategory.as_view(), name="postbycategory"),
]
