from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente,Transaction

# Create your views here.
def index(request):
    return HttpResponse(":::::::Welcome to my site::::::::")

def list_clientes(request):
   # return HttpResponse("Here you find a list of people")
   users = Cliente.objects.all()
   return render(request,'finance/list_clientes.html',{'users':users})

def list_transacciones(request):
   # return HttpResponse("Here you find a list of people")
   users = Transaction.objects.all()
   return render(request,'finance/transaction.html',{'users':users})





def create_user(request):
    return HttpResponse("Here you find a list of people")




# Create your views here.
