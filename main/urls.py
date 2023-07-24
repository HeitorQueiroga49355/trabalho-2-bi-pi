from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from produto.views import produto_criar,index,crud,produto_listar,produto_editar,produto_remover, produto_detalhe
from marca.views import marca_criar,marca_listar,marca_editar,marca_remover

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adm/', crud, name="crud"),
    path('adm/produto/criar',produto_criar,name='produto_criar'),
    path('adm/produto/editar/<int:id>/',produto_editar, name='produto_editar'),
    path('adm/produto/remover/<int:id>/',produto_remover,name='produto_remover'),
    path('adm/produto/listar',produto_listar,name='produto_listar'),
    path('adm/marca/listar', marca_listar, name="marca_listar"),
    path('adm/marca/criar',marca_criar,name='marca_criar'),
    path('adm/marca/editar/<int:id>/',marca_editar, name='marca_editar'),
    path('amd/marca/remover/<int:id>/',marca_remover,name='marca_remover'),
    path('',index,name='home'),
    path('produto/<int:id>/',produto_detalhe,name='produto_detalhe'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
