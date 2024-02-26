import os
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from openpyxl import load_workbook
from .models import CleanlinessLevel, Contaminant, Damage, Material, WorkOrder, Item, WorkOrderItem, BubblePointLog, \
    LabLog, LabLogItem, ItemType, Manufacturer, Status, Location, Fitting, LabLogFitting, WorkOrderFitting, FittingSize, \
    Customer


@staff_member_required
def download_work_order_report(request, work_order_id):
    # Ensure the work order exists and handle permissions
    work_order = get_object_or_404(WorkOrder, pk=work_order_id)

    # Assuming generate_work_order_excel_report is updated as previously described
    file_path = generate_work_order_excel_report(work_order_id)

    with open(file_path, 'rb') as excel_file:
        response = HttpResponse(excel_file.read(),
                                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="work_order_{work_order_id}_report.xlsx"'
        return response

def generate_work_order_excel_report(work_order_id):
    # Load the work order with related objects
    work_order = WorkOrder.objects.filter(pk=work_order_id).select_related('status', 'location', 'customer').first()
    # Fetch all related WorkOrderItems for this WorkOrder
    work_order_items = WorkOrderItem.objects.filter(work_order=work_order).select_related('item')


    template_path = 'staticfiles/report_template/work_order_template.xlsx'
    report_path = f'work_order_{work_order.pk}_report.xlsx'

    # Load the template
    wb = load_workbook(template_path)
    ws = wb.active  # Assuming you're working with the first sheet

    # Here, you'd fill out the workbook with your work order's data
    # For example:
    ws['A1'] = f'Work Order ID: {work_order.pk}'
    # Fill in more fields as needed based on your template and work order details

    # Save the filled report to a new file
    wb.save(report_path)
    return report_path


class WorkOrderItemInline(admin.TabularInline):
    model = WorkOrderItem
    extra = 1
    fields = ['item']
    autocomplete_fields = ['item']  # Replace 'item' with the correct field name if different


class LabLogItemInline(admin.TabularInline):
    model = LabLogItem
    extra = 1  # Adjust as needed
    # Define fields and other properties as needed


class WorkOrderFittingInLine(admin.TabularInline):
    model = WorkOrderFitting
    extra = 1


class LabLogAdmin(admin.ModelAdmin):
    list_display = ('lab_log_id', 'date_logged', 'cleanliness_level')  # Adjust fields as needed
    list_filter = ('cleanliness_level',)  # Adjust or add more filters as needed
    search_fields = ('cleanliness_level', 'date_logged')  # Adjust search fields as needed
    # inlines = [LabLogItemInline]  # Include this only if you defined the LabLogItemInline



# Define the custom admin class for work order
class WorkOrderAdmin(admin.ModelAdmin):
    list_display = ('work_order_id', 'date_created', 'description', 'cleanliness_level', 'need_by_date')
    list_filter = ('cleanliness_level',)
    search_fields = ('description', 'comment')
    readonly_fields = ('work_order_id',)  # Make the work_order_id field read-only
    inlines = [WorkOrderItemInline, WorkOrderFittingInLine]
    change_form_template = 'admin/inventory/workorder/change_form.html'



class ItemAdmin(admin.ModelAdmin):
    list_display = ('mars_id', 'item_name', 'item_type', 'model_number', 'manufacturer', 'serial_number')
    search_fields = ['mars_id', 'item_name', 'description']  # You can adjust the fields as needed


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'point_of_contact', 'phone_number', 'customer_address']


# Register models with their respective admin classes
admin.site.register(CleanlinessLevel)
admin.site.register(Contaminant)
admin.site.register(Damage)
admin.site.register(Material)
admin.site.register(WorkOrder, WorkOrderAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemType)
admin.site.register(BubblePointLog)
admin.site.register(LabLog, LabLogAdmin)
admin.site.register(LabLogItem)
admin.site.register(Manufacturer)
admin.site.register(Status)
admin.site.register(Location)
admin.site.register(LabLogFitting)
admin.site.register(WorkOrderFitting)
admin.site.register(Fitting)
admin.site.register(FittingSize)
admin.site.register(Customer, CustomerAdmin)
