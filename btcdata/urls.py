
from btcdata import views
from django.urls import path, include


urlpatterns = [
    path('', views.btcdata, name='btc_table'),
    path('btchistory/', views.BtcViewSet.as_view(), name='btchistory'),
]
