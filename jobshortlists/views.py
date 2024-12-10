import django_filters
from django import forms
from django.http import HttpRequest
from django.shortcuts import HttpResponse, render
from django.contrib import messages
from django_htmx.http import trigger_client_event


from jobshortlists.forms import JobApplicationModelForm
from jobshortlists.models import Company

# Create your views here.


def hx_joblist_form(request: HttpRequest):

    context = dict()

    if request.method == "POST":
        form: forms.ModelForm = JobApplicationModelForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Job Successfully Submitted!")
        else:
            messages.error(request, "There were some errors in the form!")

    else:
        form: forms.ModelForm = JobApplicationModelForm()

    context['form'] = form

    return render(request, "forms/add_new_job.html", context=context)


class EmptyStringFilter(django_filters.CharFilter):
    def filter(self, qs, value):
        if not value:
            return qs.none()
        return super().filter(qs, value)


class CompanyFilter(django_filters.FilterSet):
    company_name = EmptyStringFilter(
        field_name="name",
        lookup_expr="icontains"
    )

    class Meta:
        model = Company
        fields = ['name']


def hx_company_filter(request: HttpRequest):
    """
    Give the companies by their name
    """

    filter = CompanyFilter(request.POST, queryset=Company.objects.all())

    return render(request, "partials/search_output.html", {"filter": filter})


def hx_company_add(request: HttpRequest):
    """
    Dynamically add new company.
    """

    company_name: str | None = request.POST.get('company_name')

    res = HttpResponse()

    if company_name:
        company = Company.objects.create(name=company_name)

        return trigger_client_event(
            res,
            "company_added",
            {"id": company.id}
        )

    return res
