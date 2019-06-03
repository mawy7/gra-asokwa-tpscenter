import django_tables2 as tables
from .models import Tcc

class TccTable(tables.Table):
    class Meta:
        model = Tcc
        template_name = 'django_tables2/bootstrap-responsive.html'

