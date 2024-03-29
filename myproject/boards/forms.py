from django import forms
from .models import Topic, Board, Post

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(
                            attrs={'rows':5, 'placeholder': 'What is on your mind?'}

                             ),
                              max_length=4500,
                              help_text= 'The max length of the text body is 4000'
                              )
    class Meta:
        model = Topic
        fields = ('subject', 'message')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ['message',]