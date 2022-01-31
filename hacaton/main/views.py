from django.shortcuts import render, HttpResponseRedirect
from main.models import Contact

# Create your views here.
def hacaton(request):
    return render(request, "index.html")

def sendMessage(request):
    if request.method == 'POST':
        send_message = Contact()
        send_message.name = request.POST.get("name")
        send_message.email = request.POST.get("email")
        send_message.addres = request.POST.get("addres")
        send_message.message = request.POST.get("message")
        send_message.save()
        return HttpResponseRedirect('/')