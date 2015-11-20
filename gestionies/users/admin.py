# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from sorl.thumbnail.admin import AdminImageMixin

from .models import User


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):

    error_message = UserCreationForm.error_messages.update({
        'duplicate_username': 'This username has already been taken.'
    })

    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


@admin.register(User)
class UserAdmin(AdminImageMixin, AuthUserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Aditional data'), {'fields': ('name', 'dni', 'usuario_rayuela', 'foto', 'es_usuario', 'id_usuario')}),
    )
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'name', 'get_thumbnail_admin')

    def get_thumbnail_admin(self, obj):
        mini = obj.get_thumbnail('50')
        try:
            output = (
                '<div style="float:left">'
                '<a style="width:%spx;display:block;margin:0 0 10px" class="thumbnail" '
                'target="_blank" href="%s">'
                '<img src="%s"></a></div>'
            ) % (mini.width, obj.foto.url, mini.url)
        except AttributeError:
            pass
        return mark_safe(output)

    get_thumbnail_admin.short_description = _('Photo')
