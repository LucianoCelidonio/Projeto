from django.shortcuts import render


def home(request):

    # return render(request, 'receitas/pages/home.html')
    return render(request, 'receitas/pages/home.html', context={
        'name': 'Luciano',
    })


def receita1(request, id):

    # return render(request, 'receitas/pages/home.html')
    return render(request, 'receitas/pages/receita-view.html', context={
        'name': 'Luciano',
    })
