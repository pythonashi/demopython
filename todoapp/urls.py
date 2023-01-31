from . import views
from django.urls import path

urlpatterns = [

    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/',views.Tasklist.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.TaskDetail.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.Taskupdate.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>',views.Taskdelete.as_view(),name='cbvdelete')
]