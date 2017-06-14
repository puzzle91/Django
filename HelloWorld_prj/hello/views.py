from django.shortcuts import render
from .models import Contact

def say_hello(request):
    all_contacts = Contact.objects.all()
    return render(request, 'index.html', {'contacts': all_contacts})


def add_contact(request):
    if request.method == "POST":
        new = Contact()
        new.first_name = request.POST.get('first_name')
        new.last_name = request.POST.get('last_name')
        new.mobile = request.POST.get('mobile')
        new.email = request.POST.get('email')

        new.save()

        return render(request, 'contactadded.html', {'contact': new})
    else:
        return render(request, 'addcontact.html')