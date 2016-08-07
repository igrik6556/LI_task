# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractUser

from django.utils.translation import ugettext as _


class CustomUser(AbstractUser):
    """
    CustomUser class extends the default Django Auth User.
    It has all the fields and permission setting of
    Django user, but adds some additional fields.
    """
    birthday = models.DateField(
        verbose_name=_('Birthday'),
        blank=True,
        null=True,
    )


class Comment(models.Model):
    """
    Comment class implementing comments that leave users.
    """
    text = models.TextField(
        verbose_name=_('Comment text')
    )
    date = models.DateTimeField(
        verbose_name=_('Comment created'),
        default=timezone.now
    )
    user = models.ForeignKey(
        CustomUser,
        verbose_name=_('User')
    )
    parent = models.ForeignKey(
        'self',
        verbose_name=_('Parent'),
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'comments'
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return self.text[:40].rstrip()

    def get_reply_link(self):
        return reverse('comments:comment_reply', args=[self.id])
