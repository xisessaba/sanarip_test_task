from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Fermer, Culture, Season, Plot
from .serializers import FermerSerializer, CultureSerializer, SeasonSerializer, PlotSerializer

class FermerListView(generics.ListCreateAPIView):
    queryset = Fermer.objects.all()
    serializer_class = FermerSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name', 'description', 'phone']
    ordering_fields = ['name', 'phone']

class CultureListView(generics.ListCreateAPIView):
    queryset = Culture.objects.all()
    serializer_class = CultureSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name']

class SeasonListView(generics.ListCreateAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name']

class PlotListView(generics.ListCreateAPIView):
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['fermer', 'culture', 'season']
    ordering_fields = ['fermer', 'culture', 'season']
