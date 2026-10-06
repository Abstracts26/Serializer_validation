from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'stock',
            'category',
            'category_id',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Price must be greater than 0."
            )

        return value

    def validate(self, attrs):
        price = attrs.get('price',
        getattr(self.instance, 'price', None) )

        stock = attrs.get('stock',
        getattr(self.instance, 'stock', None) )

        if price> 100000 and stock < 10:
            raise serializers.ValidationError(
            "High-priced product cannot have zero stock."
            )

        return attrs