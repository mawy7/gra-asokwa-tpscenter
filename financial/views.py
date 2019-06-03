from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, UpdateView, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, render_to_response
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from datetime import datetime
from rest_framework import viewsets
from django.template import RequestContext
from django.shortcuts import render
from .models import Financial
from .forms import FinancialForm
from .serializers import FinancialSerializer
from django.views.decorators.csrf import csrf_exempt
import json

from .tables import FinancialTable
import django_tables2 as tables
from django_tables2 import RequestConfig
from django_tables2.export.views import ExportMixin
#from timeline_logger.models import TimelineLog
# Create your views here.

@login_required(login_url='/accounts/login/')
def entry(request):
    context = {}
    template = 'finentry.html'
    return render(request, template, context)
    
@login_required(login_url='/accounts/login/')
def entries(request):
    table = FinancialTable(Financial.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)
    return render(request, 'finentries.html', {'table': table})

class TableView(ExportMixin, tables.SingleTableView):
    table_class = FinancialTable
    model = Financial
    template_name = 'django_tables2/bootstrap-responsive.html'



@login_required
def submit_financial(request):

	if request.method == 'POST':
		form = FinancialForm(request.POST, request.FILES)

		if form.is_valid():
			obj = Financial()
			obj.user_id = request.user.pk
			obj.account_type = form.cleaned_data['account_type']
			obj.created_date = form.cleaned_data['created_date']
			obj.name_of_taxpayer = form.cleaned_data['name_of_taxpayer']
			obj.tin = form.cleaned_data['tin']
			obj.year = form.cleaned_data['year']
			obj.location_of_business = form.cleaned_data['location_of_business']
			obj.contact_number = form.cleaned_data['contact_number']
			obj.upload_document = form.cleaned_data['upload_document']
			obj.recieving_officer = form.cleaned_data['recieving_officer']
			obj.time_collected = form.cleaned_data['time_collected']
			#obj.user = entry_form.cleaned_data['user']
			# finally save the object in db
			obj.save()
            # After the operation was successful,
            # redirect to some other page
			return redirect('financial:submitted')

	else:  # 5
        # Create an empty form instance
		form = FinancialForm()

	return render(request, "finnewentry.html", {'created_date': 'Submit an Entry', 'form': form})



class FinancialView(UpdateView):
    template_name = "finentries.html"
    form_class = FinancialForm
    model = Financial
    success_url = reverse_lazy('financial:submitted')

    def get_context_data(self, **kwargs):
        context = super(FinancialView, self).get_context_data(**kwargs)
        context['name_of_taxpayer'] = "Financial Details"
        context['year'] = datetime.now().year
        context['contact_number'] = get_object_or_404(Financial, pk=self.kwargs['pk'])
        context['financials'] = Financial.objects.filter(user=self.request.user.pk)
        return context




class FinancialViewsSets(viewsets.ReadOnlyModelViewSet):
    serializer_class = FinancialSerializer
    queryset = Financial.objects.all()


class SuccessView(TemplateView):
    template_name = "finsuccess.html"

    def get_context_data(self, **kwargs):
        context = super(SuccessView, self).get_context_data(**kwargs)
        context['name_of_taxpayer'] = 'Entry Submission Successful'
        context['year'] = datetime.now().year
        return context


