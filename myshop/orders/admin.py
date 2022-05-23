from abc import ABC
#from django_admin_listfilter_dropdown.filters import *

from django.contrib import admin
from django.db.models import Q
from .models import Order, OrderItem
import csv
import datetime
from django.http import HttpResponse
from django.urls import reverse
from django.utils.safestring import mark_safe


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    content_disposition = f'attachment; filename= {opts.verbose_name}.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = content_disposition
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response


export_to_csv.short_description = 'Export to CSV'


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class InputFilter(admin.SimpleListFilter):
    template = 'admin/input_filter.html'

    def lookups(self, request, model_admin):
        # Dummy, required to show the filter.
        return ((),)

    def choices(self, changelist):
        # Grab only the "all" option.
        all_choice = next(super().choices(changelist))
        all_choice['query_parts'] = (
            (k, v)
            for k, v in changelist.get_filters_params().items()
            if k != self.parameter_name
        )
        yield all_choice

class Order_ID(InputFilter):
    parameter_name = 'id'
    title = 'Order ID'

    def queryset(self, request, queryset):
        if self.value() is not None:
            x = self.value()
            query = list(x.split(" "))
            for i in query:
                return queryset.filter(
                    id=i
                )
       

class First_Name_Filter(admin.SimpleListFilter):
    title = 'First Name Filter'
    parameter_name = 'first_name'

    def lookups(self, request, model_admin):
        """('The filter parameter', 'its representation in the filter list')"""

        return (
            ('tst', 'Filter by "tst"'),
            # ('test', 'test')
        )

    def queryset(self, request, queryset):
        x= self.value()
        if not x:
            return queryset
        if x == 'tst':
            return queryset.filter(first_name= x)
        # elif x == 'test':
        #     return queryset.filter(first_name= x)



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address',
                    'postal_code', 'city', 'paid', 'created', 'updated', 'order_detail', 'order_pdf']
    list_filter = ['paid', 'created', 'updated',Order_ID,First_Name_Filter]
    inlines = [OrderItemInline]
    actions = [export_to_csv]

    def order_detail(self, obj):
        url = reverse('orders:admin_order_detail', args=[obj.id])
        return mark_safe(f'<a href="{url}">View</a>')

    def order_pdf(self, obj):
        url = reverse('orders:admin_order_pdf', args=[obj.id])
        return mark_safe(f'<a href="{url}">PDF</a>')

    order_pdf.short_description = 'Invoice'
