from django.urls import path
from .views import UserCollectionDetailView, UserCollectionCreateView, UserRegisterView, UserLoginView, UserLogoutView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('collections/<int:pk>/', UserCollectionDetailView.as_view(), name='user_collection_detail'),
    path('collections/create/', UserCollectionCreateView.as_view(), name='user_collection_create'),
]