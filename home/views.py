from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import PostImage, Contact

# Create your views here.
def home(request):
    PostImages = PostImage.objects.all()
    context = {"PostImages":PostImages}
    return render(request, 'home/index.html', context)

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == "POST":
        fname = request.POST.get('first-name')
        lname = request.POST.get('last-name')
        email = request.POST.get('email')
        sub = request.POST.get('Subject')
        message = request.POST.get('message')

        con = Contact(first_name=fname,last_name=lname,email=email,subject=sub,content=message)
        con.save()

        messages.success(request, "Thanks For Mailing Us We Will Get Back To You As Soon As Posible.")

        return redirect('/')


    return render(request, 'home/contact.html')

def ImageView(request , image):
    ImageDetail = PostImage.objects.filter(sno=image).first()
    context = {"ImageDetail":ImageDetail}
    return render(request, 'home/image-detail.html', context)