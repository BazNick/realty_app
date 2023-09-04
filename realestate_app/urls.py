from django.urls import path
from .views import RealEstateOfferListView, AveragePriceView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('offers/', RealEstateOfferListView.as_view(), name='offer-list'),
    path('average-price/', AveragePriceView.as_view(), name='average-price'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
