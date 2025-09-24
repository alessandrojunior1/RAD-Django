from django.urls import path
from . import views

urlpatterns = [
    path('eco/<str:textoDigitado>', views.eco),
    path('info/', views.info)

]
