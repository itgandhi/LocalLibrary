from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
    path('activation_sent/', views.account_activation_sent, name='account_activation_sent'),
    path('signup/',views.signup,name='signup'),
    ]