from django.urls import path
from .admin import download_work_order_report, download_transmittal

app_name = 'inventory'  # Defines the namespace for these URLs

urlpatterns = [
    # Define other app-specific URLs as needed

    # URL pattern for downloading the work order report
    path('workorder/<int:work_order_id>/download_report/', download_work_order_report,
         name='download_work_order_report'),
    path('workorder/<int:work_order_id>/download_transmittal/', download_transmittal, name='download_transmittal')
]
