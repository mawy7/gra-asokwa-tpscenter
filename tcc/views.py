from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
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
from .models import Tcc
from .forms import TccForm
from .serializers import TccSerializer
from django.views.decorators.csrf import csrf_exempt
import json

from .tables import TccTable
import django_tables2 as tables
from django_tables2 import RequestConfig
from django_tables2.export.views import ExportMixin
#from timeline_logger.models import TimelineLog
# Create your views here.

@login_required(login_url='/accounts/login/')
def entry(request):
    context = {}
    template = 'entry.html'
    return render(request, template, context)
    
@login_required(login_url='/accounts/login/')
def entries(request):
    table = TccTable(Tcc.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)
    return render(request, 'tccentries.html', {'table': table})

class TableView(ExportMixin, tables.SingleTableView):
    table_class = TccTable
    model = Tcc
    template_name = 'django_tables2/bootstrap-responsive.html'



@login_required
def submit_tcc(request):
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        tcc_form = TccForm(request.POST, request.FILES)

        if tcc_form.is_valid():
            # process the data in form.cleaned_data as required
            obj = Tcc()  # gets new object
            obj.user_id = request.user.pk
            obj.created_date = tcc_form.cleaned_data['created_date']
            obj.name_of_company = tcc_form.cleaned_data['name_of_company']
            obj.tcc_number = tcc_form.cleaned_data['tcc_number'] 
            obj.date_of_collection = tcc_form.cleaned_data['date_of_collection'] 
            obj.name_of_collection = tcc_form.cleaned_data['name_of_collection']
            obj.contact_number = tcc_form.cleaned_data['contact_number']
            obj.upload_document = tcc_form.cleaned_data['upload_document']
            obj.recieving_officer = tcc_form.cleaned_data['recieving_officer']
            obj.time_collected = tcc_form.cleaned_data['time_collected']
            #obj.user = entry_form.cleaned_data['user']
            # finally save the object in db
            obj.save()
            
            return redirect('tcc:submitted')

    else:  # 5
        # Create an empty form instance
        form = TccForm()

    return render(request, "newtcc.html", {'created_date': 'Submit an Entry', 'form': form})


class TccView(UpdateView):
    template_name = "tccentries.html"
    form_class = TccForm
    model = Tcc
    success_url = reverse_lazy('tcc:submitted')

    def get_context_data(self, **kwargs):
        context = super(TccView, self).get_context_data(**kwargs)
        context['name_of_taxpayer'] = "Tcc Details"
        context['year'] = datetime.now().year
        context['number'] = get_object_or_404(Tcc, pk=self.kwargs['pk'])
        context['tccs'] = Tcc.objects.filter(user=self.request.user.pk)
        return context




class TccViewsSets(viewsets.ReadOnlyModelViewSet):
    serializer_class = TccSerializer
    queryset = Tcc.objects.all()



class SuccessView(TemplateView):
    template_name = "tccsuccess.html"

    def get_context_data(self, **kwargs):
        context = super(SuccessView, self).get_context_data(**kwargs)
        context['name_of_taxpayer'] = 'Entry Submission Successful'
        context['year'] = datetime.now().year
        return context


