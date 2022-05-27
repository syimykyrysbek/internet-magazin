from django.http import HttpResponseRedirect
from django.shortcuts import render
from main.models import Contact

def homepage3(request):
    return render(request, 'base2.html')

# Create your views here.
def homepage(request):
    return render(request, 'base.html')

def homepage2(request):
    return render(request, 'index.html')

def suit(request):
    title = 'Костюмы'
    return render(request, 'suit.html', {'title':title})


def sendContact(request):
    if request.method == 'POST':
        contact = Contact()
        contact.adress = request.POST.get('adress')
        contact.number= request.POST.get('number')
        contact.message = request.POST.get('message')
        contact.save()

        return HttpResponseRedirect('/')




