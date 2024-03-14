from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Customize the original admin.site instance
admin.site.site_header = 'APCI'  # Change the header
admin.site.index_title = 'APCI'
admin.site.site_url = '/admin'  # Change the URL path (optional)


def redirect_to_admin(request):
    return redirect('/admin/')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/', include(('inventory.urls', 'inventory'), namespace='inventory')),
    path('', redirect_to_admin, name='redirect-to-admin'),
]
