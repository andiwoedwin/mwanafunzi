from django.urls import path

from .views import RegistrationAPI, LoginAPI, UserAPI, ListCategory, DetailCategory, ListProduct, DetailProduct
from . views import *
from knox import views as knox_views
from django.conf import settings

from rest_framework.authtoken.views import obtain_auth_token
from api import views
from django.conf.urls.static import static

urlpatterns = [
    path('register/', RegistrationAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('user/', UserAPI.as_view()),
    # path('hello/', views.HelloView.as_view(), name='hello'),
    path('products', ListProduct.as_view(), name='products'),
    path('products/<int:pk>/', DetailProduct.as_view(), name='singleproduct'),

    path('categories', ListCategory.as_view(), name='categorie'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='singlecategory'),

    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)




