import django_filters

from jobshortlists.models import Company


class EmptyStringFilter(django_filters.CharFilter):
    def filter(self, qs, value):
        if not value:
            return qs.none()
        return super().filter(qs, value)


class CompanyFilter(django_filters.FilterSet):
    search_company = EmptyStringFilter(
        field_name="name",
        lookup_expr="icontains"
    )

    class Meta:
        model = Company
        fields = ['name']
