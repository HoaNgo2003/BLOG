from django.shortcuts import render

from MyFirstAccount.models import Account
def homeScreenView(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts
    return render(request, 'personal/home.html', context)