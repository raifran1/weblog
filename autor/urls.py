from django.urls import path
from . import views

app_name='autor'
urlpatterns = [
    path('editar/', views.editar_autor, name='editar_autor'),

]