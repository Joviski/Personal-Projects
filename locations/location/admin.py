from django.contrib import admin
from .models import *
import csv
import datetime
from django.http import HttpResponse
from import_export.admin import ExportActionModelAdmin
from django.urls import reverse
# Register your models here.

# def export_sheet(modeladmin, request, queryset):
#     opts = modeladmin.model._meta
#     content_disposition = f'attachment; filename= {opts.verbose_name}.csv'
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = content_disposition
#     writer = csv.writer(response)
#
#     fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
#     # Write a first row with header information
#     writer.writerow([field.verbose_name for field in fields])
#     # write data rows
#     for obj in queryset:
#         data_row = []
#         for field in fields:
#             value = getattr(obj, field.name)
#             if isinstance(value, datetime.datetime):
#                 value = value.strftime('%d/%m/%Y')
#             data_row.append(value)
#         writer.writerow(data_row)
#     return response


# export_sheet.short_description = 'Export Sheet'

admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(City)
#admin.site.register(Location)

@admin.register(Location)
class LocationAdmin(ExportActionModelAdmin):
    pass
