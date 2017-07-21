from django import forms
# Comment form
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        """
        ModelForm只要在Meta中指定model=就可以了，默认会为所有的字段创建form field
        """
        model = Comment
        # 不需要所有field,使用fields指定需要的field或使用exclude排除不需要的field.
        fields = ('name', 'email', 'body')


class SearchForm(forms.Form):
    query = forms.CharField()
