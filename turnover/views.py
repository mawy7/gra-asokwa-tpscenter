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
from .models import Turnover
from .forms import TurnoverForm
from .serializers import TurnoverSerializer
from django.views.decorators.csrf import csrf_exempt
import json

from .tables import TurnoverTable
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
    table = TurnoverTable(Turnover.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)
    return render(request, 'toentries.html', {'table': table})

class TableView(ExportMixin, tables.SingleTableView):
    table_class = TurnoverTable
    model = Turnover
    template_name = 'django_tables2/bootstrap-responsive.html'



@login_required
def submit_turnover(request):
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        turnover_form = TurnoverForm(request.POST, request.FILES)

        if turnover_form.is_valid():
            # process the data in form.cleaned_data as required
            obj = Turnover()  # gets new object
            obj.user_id = request.user.pk
            obj.created_date = turnover_form.cleaned_data['created_date']
            obj.name_of_taxpayer = turnover_form.cleaned_data['name_of_taxpayer']
            obj.tin = turnover_form.cleaned_data['tin']
            obj.year = turnover_form.cleaned_data['year']
            obj.recieving_officer = turnover_form.cleaned_data['recieving_officer']
            obj.time_collected = turnover_form.cleaned_data['time_collected']
            #obj.user = entry_form.cleaned_data['user']
            # finally save the object in db
            obj.save()
            
            return redirect('turnover:submitted')

    else:  # 5
        # Create an empty form instance
        form = TurnoverForm()

    return render(request, "newturnover.html", {'created_date': 'Submit an Entry', 'form': form})



class TurnoverView(UpdateView):
    template_name = "toentries.html"
    form_class = TurnoverForm
    model = Turnover
    success_url = reverse_lazy('turnover:submitted')

    def get_context_data(self, **kwargs):
        context = super(TurnoverView, self).get_context_data(**kwargs)
        context['name_of_taxpayer'] = "Turnover Details"
        context['year'] = datetime.now().year
        context['number'] = get_object_or_404(Turnover, pk=self.kwargs['pk'])
        context['turnovers'] = Turnover.objects.filter(user=self.request.user.pk)
        return context




class TurnoverViewsSets(viewsets.ReadOnlyModelViewSet):
    serializer_class = TurnoverSerializer
    queryset = Turnover.objects.all()



class SuccessView(TemplateView):
    template_name = "tosuccess.html"

    def get_context_data(self, **kwargs):
        context = super(SuccessView, self).get_context_data(**kwargs)
        context['name_of_taxpayer'] = 'Entry Submission Successful'
        context['year'] = datetime.now().year
        return context


