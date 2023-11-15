from django.shortcuts import render


def show_menu(request):
    return render(request, 'menu/base.html')


def show_choice(request, choice):
    return render(request, 'menu/choice.html', {'choice': choice})
