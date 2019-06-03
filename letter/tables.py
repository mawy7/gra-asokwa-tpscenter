import django_tables2 as tables
from .models import Letter

class LetterTable(tables.Table):
    class Meta:
        model = Letter
        template_name = 'django_tables2/bootstrap-responsive.html'

