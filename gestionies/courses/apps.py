#  require django >= 1.7
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CoursesConfig(AppConfig):
    name = 'gestionies.courses'
    verbose_name = _('Courses')
