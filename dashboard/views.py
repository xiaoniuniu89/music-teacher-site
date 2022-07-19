from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request, 'dashboard/main.html')

@login_required
def agenda(request):
    return render(request, 'dashboard/partials/agenda.html')



    