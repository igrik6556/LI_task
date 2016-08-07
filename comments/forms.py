# -*- coding: utf-8 -*-
from django import forms
from comments.models import Comment

from django.utils.translation import ugettext as _


class CommentForm(forms.ModelForm):
    """
    It implements a form to leave and respond comments.
    """
    class Meta:
        model = Comment
        fields = ['text', 'parent']
        widgets = {'text': forms.Textarea(attrs={'placeholder': _('Leave comment'),
                                                 'class': 'form-control',
                                                 'rows': 3}
                                          ),
                   'parent': forms.HiddenInput
                   }
