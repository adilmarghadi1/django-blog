from django.shortcuts import render


def  index(request):
    return render(request, 'blog/index.html')


def blog(request):
    return render(request,'blog/blog.html')


def post(request):
    return render(request, 'blog/post.html')

def contact(request):
    return render(request, 'blog/contact.html')

