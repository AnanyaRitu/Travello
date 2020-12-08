from django.shortcuts import render
from django.http import HttpResponse
from .models import destination

# Create your views here.







def index (request):
    dest1 = destination()
    dest1.name= 'Coxs Bazar'
    dest1.desc='Largets sea beach in the world'
    dest1.price= 700
    dest1.image='coxsbazar.jpg'
    dest1.offer=False

    dest2 = destination()
    dest2.name= 'Sylhet'
    dest2.desc='Beautiful tea garden'
    dest2.price= 650
    dest2.image='sylhet.jpg'
    dest2.offer=True

    dest3 = destination()
    dest3.name= 'Shajek'
    dest3.desc='Kingdom of clouds'
    dest3.price= 750
    dest3.image='shajek.jpg'
    dest3.offer=False

    #dests = [dest1, dest2, dest3]
    dests= destination.objects.all();
    return render(request,'index.html', {'dests':dests});
#def add(request):
    #value1= int (request.POST['num1'])
    #value2= int (request.POST['num2'])
    #res= value1 + value2
    #return render(request, 'result.html', {'result':res});