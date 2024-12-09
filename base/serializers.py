# serializers.py
from rest_framework import serializers
from .models import Product, SearchResult, Watchlist, TrackedProduct, PriceHistory

class SearchResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchResult
        fields = ['product_name', 'product_url', 'price', 'query', 'created_at']  # All fields included

class ProductSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Include user field for better context
    search_result = SearchResultSerializer()  # Serialize related search result if necessary

    class Meta:
        model = Product
        fields = ['id', 'user', 'created_at', 'price', 'search_result']  # Fixed field name to match `created_at`

class TrackedProductSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Include user field for context

    class Meta:
        model = TrackedProduct
        fields = ['user', 'title', 'price', 'rating', 'reviews', 'availability', 'date_scraped']  # Ensure all fields are serialized

class PriceHistorySerializer(serializers.ModelSerializer):
    product = TrackedProductSerializer()  # Use full TrackedProductSerializer for context

    class Meta:
        model = PriceHistory
        fields = ['product', 'price', 'availability', 'date_recorded']  # Serialize all relevant fields

class WatchlistSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Include user field for better clarity
    products = TrackedProductSerializer(many=True, read_only=True)  # Show related products in the watchlist

    class Meta:
        model = Watchlist
        fields = ['id', 'user', 'name', 'products', 'created_at', 'updated_at']  # Serialize all relevant fields
        read_only_fields = ['user', 'created_at', 'updated_at']
