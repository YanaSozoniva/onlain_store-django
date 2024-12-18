from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import CatalogListViews, contacts, product_detail, add_product



app_name = CatalogConfig.name

urlpatterns = [
    path('', CatalogListViews.as_view(), name='product_list'),
    path('catalog/<int:pk>/', product_detail, name='product_detail'),
    path('contacts/', contacts, name='contacts'),
    path('add_product/', add_product, name='add_product'),

]
