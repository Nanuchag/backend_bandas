from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='inicio_app'),
    path('bands/', views.get_band, name='get_bands_app'),
    path('create_band/', views.create_band,name='create_bands_app'),
    path('delete_band/<int:id>', views.delete_band, name='delete_band_app'),
    path('bands/<int:id>/', views.detail_band, name='detail_band_app'),
    path('update_band/<int:id>/', views.update_band, name='update_band_app'),
]