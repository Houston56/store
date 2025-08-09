from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('category/', views.CatalogView.as_view(), name='category_all'),
    path('category/<slug:category_slug>/', views.CatalogView.as_view(), name='category'),
    path('product/<slug:slug>', views.ProductDetailView.as_view(), name='product_detail'),
]