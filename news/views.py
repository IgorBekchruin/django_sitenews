from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from .models import Post, Category, Comment
from django.views.generic import DetailView, ListView, FormView
from .forms import CommentForm
from django.urls import reverse, reverse_lazy
from django.db.models import Count


class HomeView(View):
    def get(self, request, *args, **kwargs):
        post = Post.objects.order_by("-created_at")[0:6]
        category = Category.objects.all()
        return render(request, 'home.html', {'post': post, 'category': category,})


class PostList(ListView):
    template_name = 'news/post_list.html'
    context_object_name = 'post'
    paginate_by = 9

    def get_queryset(self):
        post = Post.objects.all().order_by('-created_at')
        return post


class PopularPostList(ListView):
    model = Post
    template_name = 'news/popular_post_list.html'
    context_object_name = 'popular_post'
    paginate_by = 9

    def get_queryset(self):
        popular_post = Post.objects.annotate(ncomment=Count('comments')).order_by('-ncomment')
        return popular_post


class PostDetailView(DetailView):
    model = Post
    template_name = 'news/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs["slug"]

        form = CommentForm()
        post = get_object_or_404(Post, slug=slug)
        popular_post = Post.objects.annotate(ncomment=Count('comments')).order_by('-ncomment')[:2]
        comments = post.comments.all()

        context['post'] = post
        context['popular_post'] = popular_post
        context['form'] = form
        context['comments'] = comments
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        post = Post.objects.get(slug=self.kwargs['slug'])
        comments = post.comments.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']

            comment = Comment.objects.create(name=name, email=email, text=text, post=post)
            
            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)

        return self.render_to_response(context=context)


class PostByCategory(ListView):
    # model = Post
    context_object_name = 'post'
    template_name = 'news/postbycategory.html'
    paginate_by = 6

    def get_queryset(self):
        # получftv категорию
        category = get_object_or_404(Category, slug__iexact=self.kwargs.get('slug'))
        # вывести новости из категории
        queryset = category.posts.all().order_by('-created_at')
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs["slug"]
        category = get_object_or_404(Category, slug=slug)
        post = category.posts.all().order_by('-created_at')

        context['post'] = post
        context['cat'] = category
        return context    