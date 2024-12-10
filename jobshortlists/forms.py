from django import forms

from jobshortlists.models import Company, JobApplication


# Create your forms here.


class JobApplicationModelForm(forms.ModelForm):
    """
    Add a new job to shortlist.
    """

    class Meta:
        model = JobApplication
        fields = [
            "status",
            "company_name",
            "job_title",
            "job_type",
            "location",
            "max_salary",
            "min_salary",
            "source",
            "job_url",
            "interest"
        ]


class HxCompanyForm(forms.ModelForm):
    """
    Form for dynamically adding company.
    """

    class Meta:
        model = Company
        fields = ['name']
