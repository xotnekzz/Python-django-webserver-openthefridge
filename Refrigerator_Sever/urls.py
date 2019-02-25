from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from Refrigerator import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'Food', views.FoodViewSet)
router.register(r'Shopping', views.ShoppingViewSet)
router.register(r'Recipe', views.RecipeViewSet)
router.register(r'Info', views.PostViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'Refrigerator_Sever.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^food/$', views.food_list, name="food_list"),
    url(r'^food/register/$', views.food_register, name="food_register"),
    url(r'^food/register/delete/(?P<pk>\d+)/$', views.food_delete, name="food_delete"),
    url(r'^food/register/(?P<pk>\d+)/$', views.register_edit, name="register_edit"),
    url(r'^shopping_list/$', views.shopping_list, name="shopping_list"),
    url(r'^shopping/register/$', views.shopping_register, name="shopping_register"),
    url(r'^shopping/register/delete/(?P<pk>\d+)/$', views.shopping_delete, name="shopping_delete"),
    url(r'^shopping/register/(?P<pk>\d+)/$', views.shopping_edit, name="shopping_edit"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
