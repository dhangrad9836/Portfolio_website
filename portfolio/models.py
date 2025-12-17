from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=10, default='🚀')
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title


class Technology(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='technologies')
    
    class Meta:
        verbose_name_plural = 'Technologies'
    
    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.category

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    excerpt = models.TextField(max_length=300, blank=True, help_text="Short description for blog list")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    featured_image = models.CharField(max_length=10, default='📝', help_text="Emoji for the blog post")
    
    class Meta:
        ordering = ['-created_date']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.excerpt:
            # Create excerpt from first 200 characters of content
            self.excerpt = self.content[:200] + '...' if len(self.content) > 200 else self.content
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('portfolio:blog_detail', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.title


class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='categories')
    
    class Meta:
        verbose_name_plural = 'Blog Categories'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name