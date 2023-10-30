from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    text = forms.CharField(
        label="Текст комментария",
        widget=forms.Textarea(
            attrs={"class": "input", "name": "message", "placeholder": "Сообщение"}
        ),
    )

    class Meta:
        model = Comment
        fields = ("text",)
