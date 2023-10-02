from django.contrib import admin
from django.urls import path

import reviewes.views

urlpatterns=[
    path('admin/', admin.site.urls),
    path('', reviewes.views.index)
]