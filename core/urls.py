from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required


from .views import HomeView, TccView, tabelaView, DefesaView

urlpatterns = [
    path('' , HomeView),
    path('tcc' , TccView),
    path('tabela' , tabelaView),
    path('defesa' , DefesaView),
]