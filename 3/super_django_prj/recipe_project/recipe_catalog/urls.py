from django.urls import path
from .views import about, recipe_list, recipe_detail

urlpatterns = [
    path('recipes/', recipe_list),
    path('recipe/<int:pk>/', recipe_detail),
    path('about/', about),
]
