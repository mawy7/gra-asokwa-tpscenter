from django.shortcuts import render, render_to_response
from django.template import RequestContext

from financial.models import Financial
from letter.models import Letter
from tcc.models import Tcc
from turnover.models import Turnover
# Create your views here.



def home(request):
    countE= Financial.objects.all().count()
    countT= Tcc.objects.all().count()
    countL= Letter.objects.all().count()
    countO= Turnover.objects.all().count()
    context= {'countE': countE, 'countT': countT, 'countL': countL, 'countO': countO}
    template = 'homepage.html'
    return render(request, template, context)




def handler404(request, exception):
    return render(request, '404.html', locals())

