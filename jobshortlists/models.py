from datetime import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _

from djmoney.models.fields import MoneyField

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class JobStatus(BaseModel):
    """
    The State of your job.
    """

    name = models.CharField(_("Status"), max_length=255)

    def __str__(self) -> str:
        return str(self.name)


class JobType(BaseModel):
    """
    Type of job.
    """

    job_type = models.CharField(_("Job Type"), max_length=255)

    def __str__(self) -> str:
        return str(self.job_type)


class Company(BaseModel):
    """
    The company you will be applying for.
    """

    name = models.CharField(_("Company"), max_length=255)

    def __str__(self) -> str:
        return str(self.name)


class JobShortlistDeck(BaseModel):
    """
    The group of the job shortlists.
    """

    name = models.CharField(_("Job Deck Name"), max_length=255)

    def __str__(self) -> str:
        return str(self.name)


class JobSkillsRequired(BaseModel):
    """
    The required skills for the job.
    """

    skill = models.CharField(_("Skill"), max_length=255)

    def __str__(self) -> str:
        return str(self.skill)


class JobApplication(BaseModel):
    """
    The details of the shortlisted job.
    """

    class JobInterest(models.TextChoices):
        HIGH = "High"
        MEDIUM = "Medium"
        LOW = "Low"

    status = models.ForeignKey(JobStatus, on_delete=models.CASCADE)
    company_name = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="companies")
    job_title = models.CharField(_("Job Title"), max_length=255)
    date_applied = models.DateField(default=datetime.now)
    closing_date = models.DateField(blank=True, null=True)
    resume_submitted = models.BooleanField(default=False)
    cover_letter_submitted = models.BooleanField(default=False)
    job_type = models.ForeignKey(JobType, on_delete=models.CASCADE)
    location = models.CharField(_("Location"), max_length=255)
    min_salary = MoneyField(max_digits=19,
                            decimal_places=4,
                            default_currency='INR', null=True)
    max_salary = MoneyField(max_digits=19,
                            decimal_places=4,
                            default_currency='INR', null=True)
    source = models.CharField(_("Source of Job"),
                              max_length=255, blank=True, null=True)
    job_url = models.URLField(blank=True, null=True)
    interest = models.CharField(max_length=255,
                                choices=JobInterest.choices,
                                null=True, blank=True)


class ResumeSubmitted(BaseModel):
    """
    The resume that was submitted to the job.
    """

    job_application = models.ForeignKey(
        JobApplication, on_delete=models.CASCADE)
    resume = models.FileField()

    def __str__(self) -> str:
        return "resume file."


class JobNotes(BaseModel):
    """
    The user notes for the job.
    """

    job_application = models.ForeignKey(
        JobApplication, on_delete=models.CASCADE)
    note = models.TextField(blank=True)

    def __str__(self) -> str:
        return str(self.note)
