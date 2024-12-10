from django.urls import path

from jobshortlists.views import hx_company_add, hx_company_filter, hx_joblist_form

urlpatterns = [
    path("hx/add/", hx_joblist_form, name="hx_add_joblist"),
    path("hx/company/search/", hx_company_filter, name="hx_company_filter"),
    path("hx/company/search/add/", hx_company_add, name="hx_company_search_add"),
]
