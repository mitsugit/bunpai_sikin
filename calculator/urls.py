from django.conf.urls import url
from django.urls import path

from. import views

urlpatterns = [
    path('',views.index,name='index'),
    path('calc',views.calc),
    path('calc2',views.calc2),
    path('gouseiodds',views.gouseiodds,name='gouseiodds'),
    path('gouseiodds_calc',views.gouseiodds_calc,name='gouseiodds_calc'),
    path('test',views.test,name='test'),
    
]
