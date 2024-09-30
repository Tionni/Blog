from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Blog, BlogPost
from .forms import BlogForm, BlogPostForm


# Create your views here.
@login_required
def index(request):
    blogs = Blog.objects.filter(owner=request.user).order_by('-date_added')
    

    context = {"blogs": blogs}
    return render(request, 'blogs/index.html', context)

def homepage(request):
    return render(request, 'blogs/home_page.html')    
@login_required
def blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    #make sure the blog belongs
    if blog.owner != request.user:
        raise Http404
    blog_posts =blog.blogpost_set.order_by('-date_added')
    context = {'blog': blog, 'blog_posts': blog_posts}
    return render(request, "blogs/blog.html", context)
@login_required
def blogpost(request, blogpost_id):
    blog_post = BlogPost.objects.get(id=blogpost_id)
    context = {'blog_post': blog_post}
    return render(request, "blogs/blogpost.html", context)
@login_required
def new_blog(request):
    """Add a new blog"""
    if request.method != 'POST' :
        #No data submitted; create a blank form
        form = BlogForm()
    else:
        #Post data submitted: process data
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect('blogs:index')
    
    #Display a blank or invalid form
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)
@login_required
def new_blogpost(request, blog_id):
    """add a blogpost for a particular blog"""
    blog = Blog.objects.get(id=blog_id)

    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_blogpost = form.save(commit=False)
            
            new_blogpost.blog = blog
            if blog.owner == request.user:
                new_blogpost.save()
            return redirect('blogs:blog', blog_id=blog_id)

    context = {'blog': blog, 'form':form} 
    return render(request, 'blogs/new_blogpost.html', context)
@login_required
def edit_blogpost(request, blogpost_id):
    """Editing an existing blog post"""
    blogpost = BlogPost.objects.get(id=blogpost_id)
    blog = blogpost.blog
    if blog.owner != request.user:
        raise Http404
    if request.method != 'POST':
        #Initial request: prefill form with the current blogpost
        form = BlogPostForm(instance=blogpost)
    else:
        #Post data submitted; process data
        form = BlogPostForm(instance=blogpost, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogpost', blogpost_id=blogpost.id)
                
    context = {'blogpost': blogpost, 'blog': blog, 'form': form}
    return render(request, 'blogs/edit_blogpost.html', context)




