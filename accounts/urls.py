from django.urls import path
from . import views
from autor.views import cadastro_autor
from django.contrib.auth import views as auth_views

app_name='accounts'
urlpatterns = [
    path('concluir/cadastro/?P<int:id_autor>/', views.add_user, name='add_user'),
    path('logout-usuario/', views.user_logout, name='user_logout'),
    path('login-usuario/', views.user_login, name='user_login'),
    path('alterar-senha/', views.alterar_senha, name='alterar_senha'),
    path('editar-usuario/', views.editar_user, name='editar_user'),
    path('cadastro/autor/', cadastro_autor, name='cadastro_autor'),

]