from django.urls import path
from .views import * 


urlpatterns = [
   path('',Index.as_view(),name='index'),
   path('<pk>/update',update.as_view(),name='update'),
   path('<pk>/delete',delete.as_view(),name='delete'),
]
