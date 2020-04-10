from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('holiday/', include('holiday.urls')),
    path('admin/', admin.site.urls),
]
