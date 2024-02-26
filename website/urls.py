from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_admin(request):
    return redirect('/admin/')

urlpatterns = [
    path('', redirect_to_admin, name='redirect-to-admin'),
    path('admin/', admin.site.urls),
    # Include 'inventory' app URLs with namespace
    path('inventory/', include(('inventory.urls', 'inventory'), namespace='inventory')),
]
