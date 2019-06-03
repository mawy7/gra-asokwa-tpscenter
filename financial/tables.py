import django_tables2 as tables
from .models import Financial

class FinancialTable(tables.Table):
    class Meta:
        model = Financial
        template_name = 'django_tables2/bootstrap-responsive.html'

