from .models import Inventory
from .serializers import InventorySerializer
from rest_framework.viewsets import GenericViewSet
from django.views.generic import ListView, DetailView, TemplateView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
import requests
from django.conf import settings
from urllib.parse import urljoin

INVENTORY_SEARCH_FIELDS = ['inventory_id','inventory_name', 'inventory_description', 'inventory_note', 'inventory_supplier__supplier_name', 'inventory_availability']

class InventoryViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = INVENTORY_SEARCH_FIELDS
    search_fields = INVENTORY_SEARCH_FIELDS
    ordering_fields = ['inventory_name', 'inventory_stock', 'inventory_availability']

    def get_queryset(self):
        queryset = super().get_queryset()
        supplier_id = self.request.query_params.get('supplier_id')
        if supplier_id:
            queryset = queryset.filter(inventory_supplier_id=supplier_id)
        return queryset

class InventoryListView(TemplateView):
    template_name = 'inventory/inventory_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        search_query = self.request.GET.get('search', '')
        
        # Construct API URL with search parameter if present
        api_url = urljoin(settings.BASE_URL, '/api/inventory/')
        if search_query:
            api_url += f'?search={search_query}'
        
        # Fetch data from API
        response = requests.get(api_url)
        inventories = response.json()
        
        # Add detail URL to each inventory
        for inventory in inventories:
            inventory['detail_url'] = self.request.build_absolute_uri(
                f'/inventory/detail/{inventory["inventory_id"]}/'
            )
            
        context['inventories'] = inventories
        context['search_query'] = search_query
        return context

class InventoryDetailView(TemplateView):
    template_name = 'inventory/inventory_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        inventory_id = kwargs.get('pk')
        
        # Fetch single inventory item from API
        api_url = urljoin(settings.BASE_URL, f'/api/inventory/{inventory_id}/')
        response = requests.get(api_url)
        context['inventory'] = response.json()
        return context
        