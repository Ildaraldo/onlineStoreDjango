from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('', views.catalog_list, name='catalog_list'),
    path('', views.catalog_list),
    re_path(r'^contacts', views.contact_list),
]
