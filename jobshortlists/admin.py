from django.contrib import admin

from jobshortlists.models import Company, JobApplication, JobNotes, JobSkillsRequired, JobStatus, JobType, ResumeSubmitted

# Register your models here.
admin.site.register(JobStatus)
admin.site.register(JobType)
admin.site.register(Company)
admin.site.register(JobSkillsRequired)
admin.site.register(JobApplication)
admin.site.register(ResumeSubmitted)
admin.site.register(JobNotes)
