from rest_framework import serializers
from .models import Food, Shopping, Info, Recipe


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields=('url','food_number','food_type', 'food_name', 'food_purchase', 'food_exdate', 'food_location', 'food_image')

class ShoppingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shopping
        fields=('url','shopping_id','food_type', 'shopping_name', 'shopping_memo')

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields=('image','link','title')

class PostSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Info
            fields = ('id','title', 'post', 'image')