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
    path("", cache_page(60 * 5)(HomeView.as_view()), name="home"),
    path("posts", cache_page(60 * 10)(PostList.as_view()), name="post_list"),
    path(
        "popular_post",
        cache_page(60 * 10)(PopularPostList.as_view()),
        name="popular_post_list",
    ),
    path(
        "post/<slug:slug>",
        cache_page(60 * 20)(PostDetailView.as_view()),
        name="post_detail",
    ),
    path(
        "post/tags/<str:tag>/",
        cache_page(60 * 10)(PostByTagListView.as_view()),
        name="post_by_tags",
    ),
    path(
        "post/category/<slug:slug>/",
        cache_page(60 * 10)(PostByCategory.as_view()),
        name="postbycategory",
    ),
]
