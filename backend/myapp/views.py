from django.shortcuts import render, HttpResponse
from .models import freelanceOrder
from .forms import orderUploadForm

from django.views.generic import TemplateView

# Create your views here.
def home(request):
    return render(request, "home.html")

def orders(request):
    orderItems = freelanceOrder.objects.all()
    return render(request, "orders.html", {"orders": orderItems})

def orderUpload(request):
    if request.POST:
        form = orderUploadForm(request.POST, request.FILES)
        print(request.FILES)

        if form.is_valid():
            form.save()

    return render(request, "orderUpload.html", {"form" : orderUploadForm})

class test(TemplateView):
    template_name = "testingVue.html"
