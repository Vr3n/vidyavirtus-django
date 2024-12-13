from core.customizations.forms import TailwindModelForm
from jobshortlists.models import Company, JobApplication, JobStatus, JobType


# Create your forms here.


class JobApplicationModelForm(TailwindModelForm):
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
            "interest",
            "job_description",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Setting the queryset for fk fields.
        self.fields['status'].queryset = JobStatus.objects.all()
        self.fields['company_name'].queryset = Company.objects.all()
        self.fields['job_type'].queryset = JobType.objects.all()


class HxCompanyForm(TailwindModelForm):
    """
    Form for dynamically adding company.
    """

    class Meta:
        model = Company
        fields = ['name']
