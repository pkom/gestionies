# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from sorl.thumbnail import ImageField
from django_auth_ldap.backend import populate_user

#en django 1.7 no funciona AUTH_PROFILE_MODULE actualizamos datos mediante este signal
def update_user(sender, user=None, ldap_user=None, **kwargs):

    # Remember that every attribute maps to a list of values
    dni = ldap_user.attrs.get("employeeNumber", [])
    uid = ldap_user.attrs.get("uid", [])
    #profe = user.profesor
    if dni:
        user.dni = dni[0]
    if uid:
        user.usuario_rayuela = uid[0]
    user.save()

populate_user.connect(update_user)


def upload_to(instance, filename):
    return '/'.join(['users', instance.user.username, filename])


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    dni = models.CharField(blank=True, max_length=20, db_index=True)
    usuario_rayuela = models.CharField(blank=True, max_length=50)
    foto = ImageField(upload_to=upload_to, blank=True)
    es_usuario = models.BooleanField(default=False)
    id_usuario = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})


