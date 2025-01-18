from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    CatalogListViews,
    ContactViews,
    CatalogDetailViews,
    CatalogCreateView,
    CatalogDeleteView,
    CatalogUpdateView,
    UnpublishProductView,
)


app_name = CatalogConfig.name

urlpatterns = [
    path("", CatalogListViews.as_view(), name="product_list"),
    path("catalog/<int:pk>/", CatalogDetailViews.as_view(), name="product_detail"),
    path("contacts/", ContactViews.as_view(), name="contacts"),
    path("catalog/create/", CatalogCreateView.as_view(), name="product_create"),
    path("catalog/<int:pk>/delete/", CatalogDeleteView.as_view(), name="product_delete"),
    path("catalog/<int:pk>/update/", CatalogUpdateView.as_view(), name="product_update"),
    path('catalog/unpublish/<int:pk>/', UnpublishProductView.as_view(), name='unpublish_product'),

]
