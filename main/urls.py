from django.urls import path
# from .class_views import *
from .views import *

urlpatterns=[
    path('list/',list,name='list'),
    path('list/<int:pk>/',detail,name='detail'),
    path('create/',create,name='create'),
    path('update/<int:pk>/',update,name='update'),
    path('delete/<int:pk>/',delete,name='delete'),
    path('logout/',logout_view,name='logout')





    # '''
    # QUYIDAGILAR  CLASS VIEW
    # '''
    # path('list/',List.as_view(), name='list'),
    # path('create/',Create.as_view(),name='create'),
    # path('update/<int:pk>/',Update.as_view(),name='update'),
    # path('delete/<int:pk>/',delete,name='delete'),
    # path('list/<int:pk>/',Detail.as_view(),name='detail'),
    # path('test/',test,name='test'),
]