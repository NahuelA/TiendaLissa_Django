from django.urls import path

# My views
from tienda_lissa_app import views
# Urls from tienda lissa app
urlpatterns = [
    # Sales
    path('testing-funct/', views.tests),
    path('redir', views.Redirecting.as_view(), name='redirecting-my-view')
]