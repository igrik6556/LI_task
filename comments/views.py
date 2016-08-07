# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from comments.models import Comment
from comments.forms import CommentForm
from comments.utils import create_tree


def main(request):
    """
    Display comment desk with form for comment.
    """
    c = Comment.objects.all()
    form = CommentForm()
    return render_to_response('comments/main.html',
                              {
                                  'user': request.user,
                                  'comments': create_tree(c),
                                  'form': form,
                                  'num_comments': c.count(),
                              },
                              RequestContext(request))


def add_comment(request, **kwargs):
    """
    Displays form for add comment.
    """
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.user = request.user
            try:
                c.parent = Comment.objects.get(id=kwargs['pk'])
            except KeyError:
                pass
            c.save()
            return redirect('comments:main')
    else:
        form = CommentForm()
    return render_to_response('comments/add_comment_page.html',
                              {
                                  'form': form,
                              },
                              RequestContext(request))


def custom_404(request):
    return render(request, 'errors/404.html', {}, status=404)

