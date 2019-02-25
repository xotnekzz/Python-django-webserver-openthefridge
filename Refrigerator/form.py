from django import forms
from .models import Food, Shopping

class FoodForm(forms.ModelForm):
      class Meta:
          model = Food
          fields = ('food_type', 'food_number', 'food_name', 'food_purchase', 'food_exdate',  'food_location' )


class ShoppingForm(forms.ModelForm):
      class Meta:
          model = Shopping
          fields = ('food_type', 'shopping_name', 'shopping_memo' )



