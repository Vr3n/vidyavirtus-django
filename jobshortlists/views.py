from django import forms
from django.http import HttpRequest
from django.shortcuts import HttpResponse, render
from django.contrib import messages
from django_htmx.http import trigger_client_event


from jobshortlists.filters import CompanyFilter
from jobshortlists.forms import JobApplicationModelForm
from jobshortlists.models import Company, JobStatus, JobType

# Create your views here.


def hx_joblist_form(request: HttpRequest):
    context = dict()

    context['job_statuses'] = JobStatus.objects.all()
    context['job_types'] = JobType.objects.all()

    if request.method == "POST":
        form: forms.ModelForm = JobApplicationModelForm(request.POST)

        if form.is_valid():
            form.save()
            res = HttpResponse()

            res = trigger_client_event(
                res,
                "message",
                {"type": "success",
                 "message": "Job added to shortlist succesfully!"}
            )

            res = trigger_client_event(
                res,
                "job_added",
            )
            return res
        else:
            context['form'] = form
            res = render(request, "forms/add_new_job.html", context=context)

            return trigger_client_event(
                res,
                "message",
                {
                    "type": "error",
                    "message": form.errors.as_text()
                }
            )

    else:
        form: forms.ModelForm = JobApplicationModelForm()

    context['form'] = form

    return render(request, "forms/add_new_job.html", context=context)


def hx_company_filter(request: HttpRequest):
    """
    Give the companies by their name
    """

    filter = CompanyFilter(request.POST, queryset=Company.objects.all())

    return render(
        request,
        "partials/company_search_output.html",
        {"filter": filter}
    )


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
