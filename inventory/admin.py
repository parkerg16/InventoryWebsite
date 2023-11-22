from django.contrib import admin
from .models import CleanlinessLevel, Contaminant, Damage, Material, WorkOrder, Item, WorkOrderItem, BubblePointLog, \
	LabLog, LabLogItem, ItemType, Manufacturer, Status, Location, Fitting, LabLogFitting, WorkOrderFitting, FittingSize\



# Define the custom admin class for WorkOrderItem
class WorkOrderItemInline(admin.TabularInline):
	model = WorkOrderItem
	extra = 1
	fields = ['item']
	autocomplete_fields = ['item']  # Replace 'item' with the correct field name if different


# Define the custom admin class for workorder
class WorkOrderAdmin(admin.ModelAdmin):
	list_display = ('work_order_id', 'date_created', 'description', 'cleanliness_level', 'need_by_date')
	list_filter = ('cleanliness_level',)
	search_fields = ('description', 'comment')
	inlines = [WorkOrderItemInline]


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
admin.site.register(LabLog)
admin.site.register(LabLogItem)
admin.site.register(Manufacturer)
admin.site.register(Status)
admin.site.register(Location)
admin.site.register(LabLogFitting)
admin.site.register(WorkOrderFitting)
admin.site.register(Fitting)
admin.site.register(FittingSize)
