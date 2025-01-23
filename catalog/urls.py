from django.urls import path
from django.views.decorators.cache import cache_page
from catalog.apps import CatalogConfig
from catalog.views import (
    CatalogListViews,
    ContactViews,
    CatalogDetailViews,
    CatalogCreateView,
    CatalogDeleteView,
    CatalogUpdateView,
    UnpublishProductView,
    CategoryListViews,
    CategoryProductsDetailView,
)


app_name = CatalogConfig.name

urlpatterns = [
    path("", CatalogListViews.as_view(), name="product_list"),
    path("catalog/<int:pk>/", cache_page(60 * 10)(CatalogDetailViews.as_view()), name="product_detail"),
    path("contacts/", ContactViews.as_view(), name="contacts"),
    path("catalog/create/", CatalogCreateView.as_view(), name="product_create"),
    path("catalog/<int:pk>/delete/", CatalogDeleteView.as_view(), name="product_delete"),
    path("catalog/<int:pk>/update/", CatalogUpdateView.as_view(), name="product_update"),
    path("catalog/unpublish/<int:pk>/", UnpublishProductView.as_view(), name="unpublish_product"),
    path("catalog/category/", CategoryListViews.as_view(), name="category_list"),
    path(
        "catalog/product_category/<int:pk>/",
        cache_page(60 * 10)(CategoryProductsDetailView.as_view()),
        name="product_category",
    ),
]
