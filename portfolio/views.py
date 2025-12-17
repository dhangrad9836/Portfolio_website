from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Project, Skill, BlogPost

def home(request):
    projects = Project.objects.all()[:3]  # Get top 3 projects
    skills = Skill.objects.all()
    recent_posts = BlogPost.objects.filter(published=True)[:3]  # Get 3 recent blog posts
    
    context = {
        'projects': projects,
        'skills': skills,
        'recent_posts': recent_posts,
    }
    return render(request, 'portfolio/home.html', context)


def blog_list(request):
    posts = BlogPost.objects.filter(published=True)
    paginator = Paginator(posts, 6)  # Show 6 posts per page
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'portfolio/blog_list.html', context)


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    
    # Get related posts (same author or recent)
    related_posts = BlogPost.objects.filter(
        published=True
    ).exclude(id=post.id)[:3]
    
    context = {
        'post': post,
        'related_posts': related_posts,
    }
    return render(request, 'portfolio/blog_detail.html', context)