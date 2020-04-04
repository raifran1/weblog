from django.urls import path
from . import views

app_name='autor'
urlpatterns = [
    path('postar/', views.cadastro_post, name='cadastro_post'),
    path('editar/post/<int:id_post>/', views.editar_post, name='editar_post'),
    path('', views.posts, name='posts'),
    path('postagens/autor/', views.posts_autor, name='posts_autor'),
    path('deletar/post/<int:id_post>/', views.deletar_post, name='deletar_post')
]