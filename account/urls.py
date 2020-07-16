from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import Account, ObtainTokenPairWithColorView

urlpatterns = [
    path('user/', Account.as_view(), name="create_user"),
    path('user/login/', ObtainTokenPairWithColorView.as_view(), name='token_create'),
    path('user/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/logout/', jwt_views.TokenRefreshView.as_view(),
         name='token_invalidate'),
]
