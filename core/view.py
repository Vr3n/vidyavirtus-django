from django.shortcuts import render
from django.http import HttpRequest

from jobshortlists.models import Company


def index(request: HttpRequest):

    companies = Company.objects.all()

    return render(request, 'index.html', {'companies': companies})
