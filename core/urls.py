
from django.urls import path, include
from core import views
from .views import MyTokenObtainPairView
from . serializers import MyTokenObtainPairSerializer

from rest_framework_simplejwt.views import (
    #TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('items/', views.ItemsListView.as_view() ),
    path('<slug:slug>/items/', views.CategoryItemsView.as_view() ),
    path('category/<slug:slug>/', views.CategoryView.as_view() ),
    path('categories/', views.CategoryListView.as_view() ),
    path('items/add/', views.OrderItemsView.as_view() ),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
