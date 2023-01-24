from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    name = forms.CharField(label='Ваше имя', widget=forms.TextInput(attrs={'class': 'input', "type": "text", "name": "name"}))
    email = forms.CharField(label='Ваш email', widget=forms.EmailInput(attrs={'class': 'input', "type": "email", "name": "email"}))
    text = forms.CharField(label='Текст комментария', widget=forms.Textarea(attrs={"class": "input", "name": "message", "placeholder": "Сообщение"}))
    
    class Meta:
        model = Comment
        fields = ('name', 'email', 'text')