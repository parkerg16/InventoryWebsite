from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import CleanlinessLevel, Contaminant, Damage, Material, WorkOrder, Item, WorkOrderItem, BubblePointLog, \
    LabLog, LabLogItem, ItemType, Manufacturer, Status, Location, Fitting, LabLogFitting, WorkOrderFitting, FittingSize \
 \
    # Define the custom admin class for WorkOrderItem


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

    def response_change(self, request, obj):
        if "_saveasnew" in request.POST:
            return HttpResponseRedirect(reverse('admin:reports_workorderreport_change', args=(obj.id,)))
        return super().response_change(request, obj)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('mars_id', 'item_name', 'item_type', 'model_number', 'manufacturer', 'serial_number')
    search_fields = ['mars_id', 'item_name', 'description']  # You can adjust the fields as needed


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
