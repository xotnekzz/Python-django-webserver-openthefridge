from django.db import models

FOOD_TYPES = [ ('육류','육류'),('어류','어류'),('과일류','과일류'),('야채류','야채류'),('유제품류','유제품류'),('음료류','음료류'),('소스류','소스류'),]
FOOD_LOCATION = [('냉장','냉장'),('냉동','냉동'),('실온','실온'),]

# Create your models here.
class Food(models.Model):
    food_type = models.CharField(max_length=10)
    food_number = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    food_name = models.CharField(max_length=15)
    food_purchase = models.CharField(max_length=15)
    food_exdate = models.CharField(max_length=15)
    food_location = models.CharField(max_length=10)
    food_image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.food_name

class Shopping(models.Model):
    shopping_id =  models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    food_type = models.CharField(max_length=5, choices=FOOD_TYPES)
    shopping_name = models.CharField(max_length=15)
    shopping_memo = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.shopping_name


class Recipe(models.Model):
    image = models.URLField()
    link = models.URLField()
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Info(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    title = models.CharField(max_length=30)
    post = models.TextField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

class Memo(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    title = models.CharField(max_length=3000)
    memo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    memo = models.ForeignKey(Memo)
    author = models.CharField(max_length=10)
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


