from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm

# Create your views here.

def index(request):
    all_blogs= Blog.objects.all().order_by('-data')
    return render(request, 'index.html', {'all_blogs': all_blogs})

def add(request):
    if request.method == 'POST':
        title=request.POST['title']
        body=request.POST['body']
        
        form=Blog(title=title, body=body)
        form.save()
        return redirect("index")    
    return render(request, 'add.html')

def blog(request, id):
    single_blog=Blog.objects.get(id=id)
    return render(request, 'blog.html', {'single_blog': single_blog})

def remove(request, id):
    single_blog=Blog.objects.get(id=id)
    single_blog.delete()
    return redirect('index')



def edit(request, id):
    single_blog=Blog.objects.get(id=id)
    form=BlogForm(instance=single_blog)   
    if request.method == "POST":
        form=BlogForm(request.POST, instance=single_blog)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'edit.html', {'form':form})
        
        
    

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')