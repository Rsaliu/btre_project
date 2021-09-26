from django.urls import path

from . import views

urlpatterns=[
path('version',views.get_version,name='firmware_version'),
path('download',views.download,name='download')
]