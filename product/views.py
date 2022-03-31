from django.shortcuts import render
from .models import BC

# Create your views here.
def home(request):
    name ="welcome"

    obj = BC.objects.get(id=4)
    context = {'name':name,
    'obj':obj}
    return render(request,'home.html',context)