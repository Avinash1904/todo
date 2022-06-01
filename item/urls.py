from django.urls import include, path
from .views import ItemCreateView, ItemDeleteView, ItemDetailView, ItemUpdateView, ItemsListView

urlpatterns = [
    path('items/', ItemsListView.as_view(), name='items'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('items/create/', ItemCreateView.as_view(), name='item_create'),
    path('items/update/<int:pk>', ItemUpdateView.as_view(), name='item_update'),
    path('items/delete/<int:pk>', ItemDeleteView.as_view(), name='item_delete'),
]
