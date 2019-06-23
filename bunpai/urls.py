from django.conf.urls import url
from django.urls import path

from. import views

urlpatterns = [
    path('',views.bunpai,name='bunpai'),
    path('getkaisaibi',views.getkaisaibi,name='getkaisaibi'),
    path('get_kaisai',views.get_kaisai,name='get_kaisai'),
    path('get_data',views.get_data,name='get_data'),
    # path('select_kaisaibi',views.select_kaisaibi,name='select_kaisaibi'),
    path('select',views.select,name='select'),
    path('preload',views.preload,name='preload'),
    path('sikinbunpai',views.sikinbunpai,name='sikinbunpai'),

    # path('calc',views.calc),
    # path('calc2',views.calc2),
    # path('gouseiodds',views.gouseiodds,name='gouseiodds'),
    # path('gouseiodds_calc',views.gouseiodds_calc,name='gouseiodds_calc'),
    
]
