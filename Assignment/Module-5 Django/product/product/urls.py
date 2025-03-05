from django.contrib import admin
from django.urls import path
from phones import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('company/<str:company_name>/', views.company_detail, name='company_detail'),
]
