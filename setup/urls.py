from django.contrib import admin
from django.urls import path,include 
from rest_framework import routers 
from blog.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = routers.DefaultRouter()
router.register('cadastro',UsuariosViewSet, basename='Cadastro de usuário')
router.register('publicacao',PublicacaoViewSet, basename='Publicação')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('cadastro/',ListaUsuarios.as_view()),
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
