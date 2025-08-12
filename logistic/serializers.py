from rest_framework import serializers

from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    # настройте сериализатор для продукта
    """Serializer для продукта."""
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    # product = ProductSerializer()  # Включаем информацию о продукте
    """Serializer для позиции продукта на складе."""
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']

    def create(self, validated_data):
        title_data = validated_data.pop('tilte')
        product_data = validated_data.pop('product')
        product = Product.objects.get_or_create(title=title_data)
        validated_data['product'] = product

        return super().create(validated_data)


class StockSerializer(serializers.ModelSerializer):
    """Serializer для склада."""
    positions = ProductPositionSerializer(many=True)

    # настройте сериализатор для склада

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)

        for position in positions:
            StockProduct.objects.create(
                stock=stock,
                product=position['product'],
                quantity=position['quantity'],
                price=position['price']
            )

        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')

        stock = super().update(instance, validated_data)


        for position in positions:
            StockProduct.objects.update_or_create(
                stock=stock,
                product=position['product'],
                defaults={
                    'quantity': position['quantity'],
                    'price': position['price']
                },
            )

        return stock
