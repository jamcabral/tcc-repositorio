from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required


from .views import HomeView, TccView

urlpatterns = [
    path('' , HomeView),
    path('tcc' , TccView),
]