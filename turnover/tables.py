import django_tables2 as tables
from .models import Turnover

class TurnoverTable(tables.Table):
    class Meta:
        model = Turnover
        template_name = 'django_tables2/bootstrap-responsive.html'
