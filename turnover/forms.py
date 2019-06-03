from turnover.models import Turnover
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class TurnoverForm(forms.ModelForm):

    class Meta:
        model = Turnover
        fields = ('created_date', 'name_of_taxpayer', 'tin', 'year', 'recieving_officer', 'time_collected')
    def __init__(self, *args, **kwargs):
        super(TurnoverForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_class = 'form-horizontal'


