import requests
from django.conf import settings
from urllib.parse import urljoin
from inventory.models import Inventory
from inventory.serializers import InventorySerializer
from django.views.generic import TemplateView
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

INVENTORY_SEARCH_FIELDS = [
    "inventory_id",
    "inventory_name",
    "inventory_description",
    "inventory_note",
    "inventory_supplier__supplier_name",
    "inventory_availability",
]


class InventoryViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    """
    ViewSet for handling API requests for Inventory model.
    - GenericViewSet: Provides the base set of generic view behavior
    - ListModelMixin: Adds list() method for GET requests to /api/inventory/
    - RetrieveModelMixin: Adds retrieve() method for GET requests to /api/inventory/<pk>/
    """

    # Define which database objects this ViewSet will use
    queryset = Inventory.objects.all()

    # Define which serializer to use for converting model instances to/from JSON
    serializer_class = InventorySerializer

    # Set up filtering backends for the API
    filter_backends = [
        SearchFilter,  # Enables searching (?search=term)
        OrderingFilter,  # Enables ordering (?ordering=field)
        DjangoFilterBackend,  # Enables exact filtering (?field=value)
    ]

    filterset_fields = INVENTORY_SEARCH_FIELDS
    search_fields = INVENTORY_SEARCH_FIELDS
    ordering_fields = ["inventory_name", "inventory_stock", "inventory_availability"]

    def get_queryset(self):
        """
        Override get_queryset to add custom filtering.
        This method is called whenever the API needs to get data.
        """
        # Get the base queryset from parent class
        queryset = super().get_queryset()

        # Check if supplier_id is provided in URL parameters
        # Example: /api/inventory/?supplier_id=1
        supplier_id = self.request.query_params.get("supplier_id")

        # If supplier_id is provided, filter queryset to show only
        # inventory items from that supplier
        if supplier_id:
            queryset = queryset.filter(inventory_supplier_id=supplier_id)

        return queryset


class InventoryListView(TemplateView):
    # Specify which HTML template to render for the list view
    template_name = "inventory/inventory_list.html"

    def get_context_data(self, **kwargs):
        # Override get_context_data to add custom data to template context
        context = super().get_context_data(**kwargs)

        # Get search query from URL parameters (e.g., ?search=something)
        search_query = self.request.GET.get("search", "")

        # Construct API URL with base URL from settings
        # If search query exists, append it to URL
        api_url = urljoin(settings.BASE_URL, "/api/inventory/")
        if search_query:
            api_url += f"?search={search_query}"

        # Make GET request to our own API endpoint
        # This keeps data fetching consistent between API and template
        response = requests.get(api_url)

        # Add API response data and search query to template context
        context["inventories"] = response.json()
        context["search_query"] = search_query
        return context


class InventoryDetailView(TemplateView):
    # Specify which HTML template to render for the detail view
    template_name = "inventory/inventory_detail.html"

    def get_context_data(self, **kwargs):
        # Override get_context_data to add custom data to template context
        context = super().get_context_data(**kwargs)

        # Get inventory ID from URL parameters (captured in URL pattern)
        inventory_id = kwargs.get("pk")

        # Construct API URL for specific inventory item
        api_url = urljoin(settings.BASE_URL, f"/api/inventory/{inventory_id}/")

        # Fetch single inventory item data from API
        response = requests.get(api_url)

        # Add inventory data to template context
        context["inventory"] = response.json()
        return context
