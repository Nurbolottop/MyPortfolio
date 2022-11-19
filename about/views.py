
from django.shortcuts import render,redirect
from django.core.mail import send_mail

from about.models import About, Blog,Contact

from my_works.models import Works


# Create your views here.
def index(request):
    about = About.objects.latest('id')

    context = {
        'about':about
    }

    return render(request,'index.html',context)

def about(request):
    about = About.objects.latest('id')
    context={
        'about':about
    }
    return render(request, 'about.html',context)
def contacts(request):
    about = About.objects.latest('id')
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(name = name,email = email, subject = subject,message = message)
        send_mail(

            f'{subject}',
            f'{name} Здравствуйте, спасибо за отклик, мы с вами в скором времени свяжемся. Ваше сообщение: {message} Ваши контакты: {email}, ',
            "noreply@somehost.local",
            [email]
        )
        return redirect('index')
    context = {
        'about':about
    }
    return render(request,'contact.html',context)

def portfolio(request):
   about = About.objects.latest('id')
   work = Works.objects.all()

   context = {
    'about':about,
    'work':work,

    
   } 
   return render(request,'portfolio.html',context)
def blog(request):
    about = About.objects.latest('id')
    blog = Blog.objects.all()
    context = {
        'about':about,
        'blog':blog
    }
    return render(request,'blog.html',context)

def blog_detail(request,id):
    about = About.objects.latest('id')
    new =Blog.objects.get(id = id)   

    context = {
        'new': new,
        'about': about

    }
    return render (request, 'news-details.html', context)

