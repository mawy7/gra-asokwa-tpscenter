from tcc.models import *
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class TccForm(forms.ModelForm):

    class Meta:
        model = Tcc
        fields = ( 'created_date', 'name_of_company', 'tcc_number', 'date_of_collection', 'name_of_collection', 'contact_number', 'upload_document', 'recieving_officer', 'time_collected')

    def __init__(self, *args, **kwargs):
        super(TccForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_class = 'form-horizontal'
