from django.urls import path

from products.views import ProductsListView

urlpatterns = [
    path('list', ProductsListView.as_view())
]
