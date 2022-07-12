from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from rest_framework import routers
from safaris import views


router = routers.DefaultRouter()
router.register(r'safaris', views.SafarisViewSet, basename = 'safaris')
router.register(r'tourguide', views.TourguideViewSet, basename = 'tourguide')
router.register(r'tourist', views.TouristViewSet, basename = 'tourist')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)








# from argparse import Namespace
# from django.contrib import admin
# from django.urls import path,include, re_path
# from rest_framework_simplejwt import views as jwt_views
# from django.conf import settings
# from django.conf.urls.static import static
# from safaris.models import User
# from rest_framework.routers import DefaultRouter
# from .views import *
# from rest_framework import routers
# from rest_framework_swagger.views import get_swagger_view
# from rest_framework.permissions import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# from safaris import views
 
# router = DefaultRouter()
# router.register('User', views.SignUpViewSet)
# router.register('Tourist', views.TouristViewSet)
# router.register('UpdateUserProfile', views. UpdateUserProfileViewSet)

# urlpatterns = [
#     # path('', include(router.urls)),
#     # path('api/', include(router.urls)),
#     # path('api-auth/', include('rest_framework.urls')),
#     path('tourist/', views.Tourist, name='Tourist'),
#     path('user/', views.User, name='User'),
#     path('profile/', views.Profile, name='UpdateUserProfile'),
#     path('activate/(<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
#         activate, name='activate'),
#     path('login',jwt_views.TokenObtainPairView.as_view(),name = 'login'),
#     path('run',views.HelloKenya.as_view(),name = 'HelloKenya'),
#     path('me',views.Extractor.as_view(),name = 'extract-token'),
#     path('api/safaris', views.safaris.as_view()),
#     path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
#     path('online/lipa/<phonenumber>/<amount>/', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
#     path('api/tourguide/', views.TourguideList.as_view(),name='tourguide'),
   

# ]

# #  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# #    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
# #    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
# #    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# # ]

# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


