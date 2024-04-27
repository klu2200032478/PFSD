from django.shortcuts import *
from django.http import HttpResponse
from .models import signupdetails,postdetails,contactdetails

#homepage
def home(request):
    return render(request,"home.html")
#login page
def login(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        print("test: ",email,password)
        try:
            sign1 = signupdetails.objects.filter(email=email).first()
            if sign1.password == password:
                return redirect('user')
            else:
                return HttpResponse("Invalid username or password")
        except signupdetails.DoesNotExist:
            return HttpResponse("Invalid username or password")

    return render(request,"login.html")

#signup page
def signup(request):
    return render(request,"signup.html")
def aboutus(request):
    return render(request,"aboutus.html")

def contactus(request):
    return render(request,"contactus.html")
def feedback(request):
    return render(request,"feedback.html")
def forgetpassword(request):
    return render(request, "forgetpassword.html")

#crud
def adddetails(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        sign1 = signupdetails.objects.create(name=name, email=email, password=password)

    return render(request, 'user.html')

def user(request):
    return render(request,'user.html')

def createpost(request):
    return render(request,'createpost.html')

def logout(request):
    return render(request,'home.html')

def checkdetails(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            sign1 = signupdetails.objects.get(email=email)
            if sign1.password == password:
                return redirect('user1')
            else:
                return HttpResponse("Invalid username or password")
        except signupdetails.DoesNotExist:
            return HttpResponse("Invalid username or password")

    return render(request, 'user.html')

def viewpost(request):
    s = postdetails.objects.all()
    return render(request, 'viewpost.html', {'s': s})

    # Create your views here.
def addpost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.POST.get('image')
        post = postdetails.objects.create(title=title, content=content, image=image)

    return render(request, 'createpost.html')

def profile(request):
    return render(request,'profile.html')

def addcontact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contactno = request.POST.get('contactno')
        message = request.POST.get('message')
        student = contactdetails.objects.create(name=name, email=email,contactno=contactno,message=message)
    return render(request, 'contactus.html')

def search(request):
    return render(request,'search.html')

def favorites(request):
    return render(request, 'favorites.html')

