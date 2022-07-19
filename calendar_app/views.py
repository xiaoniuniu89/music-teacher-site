from django.shortcuts import render, redirect

# Create your views here.
def calendar(request):
    if request.htmx:
        return render(request, 'calendar_app/calendar.html')
    return redirect('dashboard')