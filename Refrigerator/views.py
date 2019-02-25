from django.shortcuts import render, redirect
from rest_framework import viewsets
from Refrigerator.form import FoodForm, ShoppingForm
from Refrigerator.parse import parse_recipe
from .models import Food, Shopping, Info, Recipe
from .serializers import FoodSerializer, ShoppingSerializer, PostSerializer, RecipeSerializer


# Create your views here.

# 식재료 리스트
def food_list(request):
    food_list = Food.objects.all()
    return render(request, 'food_list.html', {
        'food_list': food_list,
    })

# 식재료 등록
def food_register(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.save(commit=False)
            food.save()
            return redirect('food_list')
    else:
            form = FoodForm()
    return render(request, 'food_form.html', {
                'form' : form,
            })

# 식재료 수정
def register_edit(request, pk):
    food = Food.objects.get(pk=pk)

    if request.method == 'POST':
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            food = form.save(commit=False)
            food.save()
            return redirect('food_list')
    else:
            form = FoodForm(instance=food)
    return render(request, 'food_form.html', {
                'form' : form,
            })

# 식재료 삭제
def food_delete(request, pk):
    del_food= Food.objects.get(pk=pk)
    del_food.delete()
    return redirect('food_list')

# 쇼핑리스트 리스트
def shopping_list(request):
    shopping_list = Shopping.objects.all()
    return render(request, 'shopping_list.html', {
        'shopping_list': shopping_list,
    })

# 식재료 등록
def shopping_register(request):
    if request.method == 'POST':
        form = ShoppingForm(request.POST)
        if form.is_valid():
            shopping = form.save(commit=False)
            shopping.save()
            return redirect('shopping_list')
    else:
            form = ShoppingForm()
    return render(request, 'shopping_form.html', {
                'form' : form,
            })

# 식재료 수정
def shopping_edit(request, pk):
    shopping = Shopping.objects.get(pk=pk)

    if request.method == 'POST':
        form = ShoppingForm(request.POST, instance=shopping)
        if form.is_valid():
            shopping = form.save(commit=False)
            shopping.save()
            return redirect('shopping_list')
    else:
            form = ShoppingForm(instance=shopping)
    return render(request, 'shopping_form.html', {
                'form' : form,
            })

# 식재료 삭제
def shopping_delete(request, pk):
    del_shopping= Shopping.objects.get(pk=pk)
    del_shopping.delete()
    return redirect('shopping_list')

# 식재료 RestFramework
class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

# 쇼핑리스트 RestFramework
class ShoppingViewSet(viewsets.ModelViewSet):
    queryset = Shopping.objects.all()
    serializer_class = ShoppingSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    #recipe_data_dict = parse_recipe()
    #for (t, l, i) in recipe_data_dict:
        #Recipe(image=i, link=l, title=t).save()
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = PostSerializer
