from django.shortcuts import render
from utils.recipes.factory import make_recipe


def home(request):

    # return render(request, 'receitas/pages/home.html')
    return render(request, 'receitas/pages/home.html', context={
        #       'name': 'Luciano',
        'recipes': [make_recipe() for _ in range(10)],
    })


def receita1(request, id):

    # return render(request, 'receitas/pages/home.html')
    return render(request, 'receitas/pages/receita-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
