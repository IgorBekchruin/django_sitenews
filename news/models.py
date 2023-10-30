from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager

from users.models import User


class Post(models.Model):
    title = models.CharField(verbose_name="Название", max_length=120)
    slug = models.SlugField()
    text = models.TextField(verbose_name="описание")
    # text=RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(upload_to="news/%Y/%m/%d", verbose_name="изображение")
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    category = TreeForeignKey(
        "Category",
        on_delete=models.PROTECT,
        related_name="posts",
        verbose_name="Категория",
    )
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    def get_comments(self):
        return self.comment_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Category(MPTTModel):
    title = models.CharField(max_length=50, unique=True, verbose_name="Название")
    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="children",
        db_index=True,
        verbose_name="Родительская категория",
    )
    slug = models.SlugField()

    class MPTTMeta:
        order_insertion_by = ["title"]

    class Meta:
        unique_together = [["parent", "slug"]]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def get_absolute_url(self):
        return reverse("postbycategory", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Комментарии"""

    username = models.ForeignKey(
        User,
        verbose_name="Комментарий",
        on_delete=models.CASCADE,
        null=True,
        related_name="comments",
    )
    text = models.TextField("Сообщение", max_length=5000)
    # parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    post = models.ForeignKey(
        Post,
        verbose_name="Комментарий",
        on_delete=models.PROTECT,
        null=True,
        related_name="comments",
    )
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ("created_at",)
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
