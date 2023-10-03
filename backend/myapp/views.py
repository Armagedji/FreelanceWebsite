from django.shortcuts import render, HttpResponse
from .models import TodoItem
from .models import freelanceOrder
from .forms import uploadForm
from .forms import orderUploadForm

# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def upload(request):
    if request.POST:
        form = uploadForm(request.POST, request.FILES)
        print(request.FILES)

        if form.is_valid():
            form.save()

    return render(request, "upload.html", {"form" : uploadForm})

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