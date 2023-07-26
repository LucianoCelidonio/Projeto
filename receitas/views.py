from django.shortcuts import render


def home(request):

    # return render(request, 'receitas/pages/home.html')
    return render(request, 'receitas/pages/home.html', context={
        'name': 'Luciano',
    })
