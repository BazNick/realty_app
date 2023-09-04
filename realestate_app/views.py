from django.db.models import Avg
from rest_framework import generics
from rest_framework.response import Response
from .models import RealEstateOffer
from .serializers import RealEstateOfferSerializer


class RealEstateOfferListView(generics.ListAPIView):
    serializer_class = RealEstateOfferSerializer

    def get_queryset(self):
        price_start = self.request.query_params.get('price_start', None)
        price_end = self.request.query_params.get('price_end', None)
        cities = self.request.query_params.get('cities', None)

        queryset = RealEstateOffer.objects.all()

        if price_start and price_end:
            queryset = queryset.filter(price__gte=price_start, price__lte=price_end)

        if cities:
            cities_list = cities.split(',')
            queryset = queryset.filter(city__name__in=cities_list)

        return queryset


class AveragePriceView(generics.GenericAPIView):
    serializer_class = RealEstateOfferSerializer

    def get(self, request):
        date_start = self.request.query_params.get('date_start', None)
        date_end = self.request.query_params.get('date_end', None)

        if not date_start or not date_end:
            return Response({'error': 'Date range is required'}, status=400)

        queryset = RealEstateOffer.objects.filter(date_start__gte=date_start, date_end__lte=date_end)
        average_price = queryset.aggregate(Avg('price'))

        return Response({'average_price': average_price})
