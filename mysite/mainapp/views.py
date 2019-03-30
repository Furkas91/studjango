from django.shortcuts import render


def index(request):
    return render(request, 'examples/home.html')


def contacts(request):
    return render(request, 'examples/contacts.html',
                  {'values': ['Если у вас остались вопрсоы обращайтесь на email:', 'email@mail.ru']})
