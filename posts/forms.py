from django import forms
from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'post_body', 'author', 'comments']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Название'
        self.fields['post_body'].label = 'Описание'
        self.fields['author'].label = 'Автор'
        self.fields['comments'].label = 'Комментарии'
