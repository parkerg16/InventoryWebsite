# inventory/urls.py

from django.urls import path
from . import views

app_name = 'inventory'  # Define the namespace

urlpatterns = [
	# ... your other URL patterns ...
	path('workorder_pdf/<int:workorder_id>/', views.workorder_pdf, name='workorder_pdf'),
]