
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from accounts.views import AdminRegisterView, TouristRegisterView


urlpatterns = [
    path("tourist/register", TouristRegisterView.as_view(), name='voter_register'),
    path("admin/register", AdminRegisterView.as_view(), name='admin_register'),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login with username and password, get access and refresh tokens in return
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),  # use this endpoint when the user access token has expired
]