# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from comments.models import Comment, CustomUser


class Test(TestCase):

    def test_add_comments(self):
        """
        This test create user and login.
        Then add comment and add reply on this comment.
        """
        c = Client()
        CustomUser.objects.create_user(username='Ihor', password='123')
        c.login(username="Ihor", password='123')

        response = c.post(reverse('comments:comment_add'), data={
            'text': 'First testing comment',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Comment.objects.filter(text='First testing comment').exists())

        response = c.post(reverse('comments:comment_reply', kwargs={'pk': 1}), data={
            'text': 'Answer on first testing comment',
            'parent': 1,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Comment.objects.filter(text='Answer on first testing comment').exists())
