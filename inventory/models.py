from django.db import models
from django.core.exceptions import ValidationError


class CleanlinessLevel(models.Model):
    cleanliness_level_id = models.AutoField(primary_key=True)
    cleanliness_level_name = models.CharField(max_length=100)
    standard = models.CharField(max_length=255)
    nvr_limit = models.FloatField()

    range_1_count_limit = models.IntegerField()
    range_2_count_limit = models.IntegerField()
    range_3_count_limit = models.IntegerField()
    range_4_count_limit = models.IntegerField()
    range_5_count_limit = models.IntegerField()

    range_1_size_limit = models.IntegerField()
    range_2_size_limit = models.IntegerField()
    range_3_size_limit = models.IntegerField()
    range_4_size_limit = models.IntegerField()
    range_5_size_limit = models.IntegerField()

    def __str__(self):
        return self.cleanliness_level_name


class Contaminant(models.Model):
    contaminant_id = models.AutoField(primary_key=True)
    particulate_bool = models.BooleanField(default=False)
    liquid_bool = models.BooleanField(default=False)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class Damage(models.Model):
    damage_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    acid_compatible = models.BooleanField(default=False)

    def __str__(self):
        return self.description


class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=100)

    def __str__(self):
        return self.status_name


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=100)

    def __str__(self):
        return self.location_name


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    customer_address = models.CharField(max_length=500)
    point_of_contact = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.customer_name} - {self.point_of_contact} - {self.phone_number}"


class WorkOrder(models.Model):
    work_order_id = models.AutoField(primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)
    cleanliness_level = models.ForeignKey(CleanlinessLevel, on_delete=models.SET_NULL, null=True)
    need_by_date = models.DateTimeField()
    comment = models.CharField(max_length=500)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.work_order_id}"


class ItemType(models.Model):
    item_type_id = models.AutoField(primary_key=True)
    item_type = models.CharField(max_length=100)
    requires_bubble_point = models.BooleanField(default=False)

    def __str__(self):
        return self.item_type


class Manufacturer(models.Model):
    manufacturer_id = models.AutoField(primary_key=True)
    manufacturer_name = models.CharField(max_length=100)
    manufacturer_description = models.CharField(max_length=255, null=True, blank=True)
    manufacturer_item_types = models.ManyToManyField(ItemType)
    manufacturer_website = models.CharField(max_length=255, null=True, blank=True)
    manufacturer_address = models.CharField(max_length=255, null=True, blank=True)
    manufacturer_image = models.ImageField(upload_to='manufacturer_logos/', null=True, blank=True)

    def __str__(self):
        return self.manufacturer_name


class FittingSize(models.Model):
    fitting_size_id = models.AutoField(primary_key=True)
    size_name = models.CharField(max_length=20)

    def __str__(self):
        return self.size_name


class Fitting(models.Model):
    fitting_id = models.AutoField(primary_key=True)
    fitting_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    lot_number = models.IntegerField()
    fitting_size = models.ForeignKey(FittingSize, on_delete=models.SET_NULL, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True, blank=True)
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Lot: {self.lot_number} - {self.fitting_size} - {self.fitting_name}"


class WorkOrderFitting(models.Model):
    work_order_fitting_id = models.AutoField(primary_key=True)
    work_order = models.ForeignKey(WorkOrder, on_delete=models.SET_NULL, null=True)
    work_order_unique_fitting = models.ForeignKey(Fitting, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"Work Order: {self.work_order}, Fitting: {self.quantity}"




# This item allows us to create a unique item without adding it to a work order so
# We can keep track of the previous times the item was cleaned.
class Item(models.Model):
    mars_id = models.CharField(primary_key=True, max_length=6)
    item_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    requires_bubble_point = models.BooleanField()
    cleanliness_level = models.ForeignKey(CleanlinessLevel, on_delete=models.PROTECT, null=True)
    item_type = models.ForeignKey(ItemType, on_delete=models.PROTECT, null=True)
    item_material = models.ForeignKey(Material, on_delete=models.PROTECT, null=True)
    model_number = models.CharField(max_length=100, blank=True, null=True)
    serial_number = models.CharField(max_length=100, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, null=True)
    in_commission = models.BooleanField(default=True)
    clean_status = models.BooleanField(default=False)
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)

    def clean(self):
        if Item.objects.filter(mars_id=self.mars_id).exists():
            raise ValidationError('An item with this MARS ID already exists.')

    def save(self, *args, **kwargs):
        self.full_clean()  # Validate the model before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.mars_id} - {self.item_name} - Model: {self.model_number} - Serial: {self.serial_number}"


# This allows us to add a unique instance of the item to a work order for history tracking
class WorkOrderItem(models.Model):
    work_order_item_id = models.AutoField(primary_key=True)
    work_order = models.ForeignKey(WorkOrder, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Item, on_delete=models.PROTECT, null=True)
    contaminant = models.ForeignKey(Contaminant, on_delete=models.PROTECT, null=True, default=None)
    damage = models.ForeignKey(Damage, on_delete=models.PROTECT, null=True, default=None)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Work Order: {self.work_order}, Item: {self.item}"


class BubblePointLog(models.Model):
    bubble_point_log_id = models.AutoField(primary_key=True)
    mars_id = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    pressure = models.FloatField()
    temperature = models.FloatField()
    bubble_one = models.FloatField()
    bubble_two = models.FloatField()
    bubble_three = models.FloatField()
    bubble_four = models.FloatField()
    average_bubble = models.FloatField()
    bubble_point = models.FloatField()
    pass_fail = models.BooleanField()

    def __str__(self):
        return f"Bubble Point Log for Item: {self.mars_id}"


class LabLog(models.Model):
    lab_log_id = models.AutoField(primary_key=True)
    cleanliness_level = models.ForeignKey(CleanlinessLevel, on_delete=models.SET_NULL, null=True)
    date_logged = models.DateTimeField(auto_now_add=True)
    work_order = models.ForeignKey(WorkOrder, on_delete=models.PROTECT, null=True)
    range_1_count = models.IntegerField()
    range_2_count = models.IntegerField()
    range_3_count = models.IntegerField()
    range_4_count = models.IntegerField()
    range_5_count = models.IntegerField()

    def __str__(self):
        return f"{self.cleanliness_level}"

class LabLogFitting(models.Model):
    lab_log_fitting_id = models.AutoField(primary_key=True)
    lab_log = models.ForeignKey(LabLog, on_delete=models.PROTECT, null=True)
    lab_log_unique_fitting = models.ForeignKey(Fitting, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)

class LabLogItem(models.Model):
    lab_log_item_id = models.AutoField(primary_key=True)
    lab_log = models.ForeignKey(LabLog, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Lab Log: {self.lab_log}, Item: {self.item}"
