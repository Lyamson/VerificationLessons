from django.shortcuts import render
from django.http import HttpResponse
from assets import database

# Create your views here.

def recipe_detail(request, pk):

    template_name = 'recipe_catalog/recipe.html'

    recipe_from_api = database.get_recipe(pk)

    if not recipe_from_api:
        return HttpResponse('Рецепт не найден')

    context = {
        'title': recipe_from_api['title'],
        'recipe_id': pk,
    }

    return render(request, template_name, context)

def recipe_list(request):
    
    template_name = 'recipe_catalog/recipes.html'

    recipes_list = database.get_recipes()

    context = {
        'recipe_list': recipes_list
    }

    return render(request, template_name, context)

def about(request):
    
    template_name = 'recipe_catalog/about.html'

    return render(request, template_name)