from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about(request):
    return HttpResponse('О проекте')

def index(request):
    return HttpResponse('Главная страница')

def recipe_detail(request, pk):

    template_name = 'recipe_catalog/recipe.html'

    title = 'Блинчики с мясом!'
    context = {
        'title': title,
        'recipe_id': pk,
    }

    return render(request, template_name, context)