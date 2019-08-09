# -*- coding: utf-8 -*-
from django import forms
from .models import ArticleColumn,ArticlePost,Comment

class ArticleColumnForm(forms.ModelForm):
    class Meta:
        model = ArticleColumn
        fields = ('column',)

class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ('title','body')

# 文章评论
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('commentator','body')