from django.urls import path

# My views
from tienda_lissa_app import views
# Urls from tienda lissa app

urlpatterns = [
    # Template home
    path('',views.ReadSales.as_view(), name='home'),
    # Templates for crud
    path('crear-ventas/',views.CreateRecordSale.as_view(), name='create-ventas'),
    path('actualizar-venta/<int:pk>/',views.UpdateRecordSale.as_view(), name='update-ventas'),
    path('confirmacion-eliminar/<int:pk>/',views.DeleteRecordSale.as_view(), name='delete-ventas')
]