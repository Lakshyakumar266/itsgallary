from django.shortcuts import render, HttpResponse
from .models import PostImage

# Create your views here.
def home(request):
    PostImages = PostImage.objects.all()
    context = {"PostImages":PostImages}
    return render(request, 'home/index.html', context)

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

def ImageView(request , image_name):

    return render(request, 'home/image-detail.html')