from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name = "polkhome"),
    path('polkadot/', views.index_page, name = 'polkadot'),
    path('polkadot/number/<int:num>/', views.number, name='number'),
    path('polkadot/upload_image/', views.upload_image, name= "upload_image")
]