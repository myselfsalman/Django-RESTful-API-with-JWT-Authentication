from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Define a simple view for the root path
def api_root(request):
    return JsonResponse({
        "message": "Welcome to the API",
        "available_endpoints": {
            "Admin Panel": "/admin/",
            "Obtain Token": "/api/token/",
            "Refresh Token": "/api/token/refresh/",
            "App API": "/api/"
        }
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('myapp.urls')),  
    path('', api_root), 
]
