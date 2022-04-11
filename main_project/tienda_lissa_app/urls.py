from django.urls import path

# My views
from tienda_lissa_app import views
# Urls from tienda lissa app
urlpatterns = [
    # Template home
    path('',views.ReadSales.as_view(), name='home'),
    # Templates for crud
    path('ventas/',views.AddSales.as_view(), name='form-ventas'),
]