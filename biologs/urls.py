from django.urls import path
from . import views

# Used in short URLs {% url 'appname:path_name' %}
app_name = 'biologs'

urlpatterns = [
    path('', views.home, name='home'),
    path('boot', views.boot, name='boot'),
    path('terminology/', views.terminology, name='terminology'),
    path('bioposts/', views.bioposts, name='bioposts'),
    path('biopost/<int:biopost_id>/', views.biopost, name='biopost'),
    path('create_biopost/', views.create_biopost, name='create_biopost'),
    path('edit_biopost/<int:biopost_id>/', views.edit_biopost, name='edit_biopost'),
    path('delete_biopost/<int:biopost_id>/', views.delete_biopost, name='delete_biopost'),
]
