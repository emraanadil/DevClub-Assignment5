from xml.etree.ElementTree import Comment
from django import forms
from .models import Lesson,Comment,Reply

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('lesson_id','name','position','video','ppt','Notes')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {'body':'comment'}
        widgets  = {
            'body':forms.Textarea(attrs={'class':'form-control','rows':4,'cols':70,'placeholder':"Enter Your comment"})
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('reply_body',)
        widgets = {
            'reply_body':forms.Textarea(attrs={'class':'form-control','rows':2,'cols':10})
        }