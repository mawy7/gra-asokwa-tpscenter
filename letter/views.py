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
from .models import Letter
from .forms import LetterForm
from .serializers import LetterSerializer
from django.views.decorators.csrf import csrf_exempt
import json

from .tables import LetterTable
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
    table = LetterTable(Letter.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)
    return render(request, 'letterentries.html', {'table': table})

class TableView(ExportMixin, tables.SingleTableView):
    table_class = LetterTable
    model = Letter
    template_name = 'django_tables2/bootstrap-responsive.html'


@login_required(login_url='/accounts/login/')
def submit_letter(request):
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        entry_form = LetterForm(request.POST, request.FILES)

        if entry_form.is_valid():
            # process the data in form.cleaned_data as required
            obj = Letter()  # gets new object
            obj.user_id = request.user.pk
            obj.created_date = entry_form.cleaned_data['created_date']
            obj.name_of_taxpayer = entry_form.cleaned_data['name_of_taxpayer']
            obj.upload_document = entry_form.cleaned_data['upload_document']
            obj.recieving_officer = entry_form.cleaned_data['recieving_officer']
            obj.time_collected = entry_form.cleaned_data['time_collected']
            #obj.user = entry_form.cleaned_data['user']
            # finally save the object in db
            obj.save()
            # After the operation was successful,
            # redirect to some other page
            return redirect('letter:submitted')
    else: 
        # Create an empty form instance
        form = LetterForm()

    return render(request, "newletter.html", {'created_date': 'Submit an Entry', 'form': form})



class LetterView(UpdateView):
    template_name = "letterentries.html"
    form_class = LetterForm
    model = Letter
    success_url = reverse_lazy('letter:submitted')

    def get_context_data(self, **kwargs):
        context = super(LetterView, self).get_context_data(**kwargs)
        context['name_of_taxpayer'] = "Letter Details"
        context['year'] = datetime.now().year
        context['number'] = get_object_or_404(Letter, pk=self.kwargs['pk'])
        context['letters'] = Letter.objects.filter(user=self.request.user.pk)
        return context


class LetterViewsSets(viewsets.ReadOnlyModelViewSet):
    serializer_class = LetterSerializer
    queryset = Letter.objects.all()



class SuccessView(TemplateView):
    template_name = "lettersuccess.html"

    def get_context_data(self, **kwargs):
        context = super(SuccessView, self).get_context_data(**kwargs)
        context['name_of_taxpayer'] = 'Entry Submission Successful'
        context['year'] = datetime.now().year
        return context
