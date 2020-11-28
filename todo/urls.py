from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'todo'

urlpatterns = [
    path('',views.index, name='index'),
    path('insert/',views.insert, name='insert'),
    path('<int:todolist_id>/', views.detail, name="detail"),
    path('<int:todolist_id>/edit/', views.edit, name='edit'),
    path('<int:todolist_id>/remove/', views.remove, name='remove'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)