from django.urls import include, path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),

]
