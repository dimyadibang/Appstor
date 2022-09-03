import django_filters
from django_filters import DateFilter, CharFilter
from .models import *


class SetoranFilter(django_filters.FilterSet):
    tglmulai = DateFilter(field_name="date_created", lookup_expr='gte')
    tglakhir = DateFilter(field_name="date_created", lookup_expr='lte')
    note = CharFilter(field_name="note", lookup_expr='icontains')

    class Meta:
        model = Setoran
        fields = '__all__'
        exclude = ['mahasantri', 'date_created']

