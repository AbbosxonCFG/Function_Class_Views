from .views import *
from django.urls import path
from .class_view import *


urlpatterns=[
    # path('list/',List.as_view()),
    # path('create/',Create.as_view()),
    # path('list/<int:pk>/',Detail.as_view()),
    # path('update/<int:pk>/',Update.as_view()),
    # path('delete/<int:pk>/',Delete.as_view()),
    


    path('list/',list_pk),
    path('create/',create),
    path('put_delete/',put_delete),
    path('signup/',SignUpView.as_view())
]