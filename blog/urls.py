from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    # path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('intro/', views.intro, name ='intro'),
    path('home/create/', views.create, name='create'),
    path('home/<int:posting_id>/update/', views.update, name='update'),
    path('home/<int:posting_id>/delete/', views.delete, name='delete'),
    path('home/<int:posting_id>/', views.evaluate, name="evaluate"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)