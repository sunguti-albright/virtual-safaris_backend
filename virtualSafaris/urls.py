from django.contrib import admin
from django.urls import path,include

from safaris import views






urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    # path('api/', include('administrator.urls')),
    path('api/', include('safaris.urls')),

    path('api/v1/online/lipa/<contact>/<amount>/', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
   
   
    
]
  
   
   
    



