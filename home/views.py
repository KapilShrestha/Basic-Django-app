from django.shortcuts import render, HttpResponse
from .forms import CustomerForm


# Create your views here.
def index(request):
    form = CustomerForm(request.POST)
    if request.method == 'POST':        
        if form.is_valid():
            form.save()
    
    context = {'form':form}
    return render(request, "index.html", context)
