from django.urls import path
from . import views

urlpatterns = [
    path('eco/<str:textoDigitado>', views.eco),
    path('info/', views.info),
    path('user/',views.user),
    path('products/', views.products),
    path('home/',views.home, name='página_home'),
    path('contato/',views.contato, name='página_de_contato'),
    path('about/',views.about, name='about')

]
