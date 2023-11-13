from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.

# view to display the home page
def home(request):
    # Retrieve the last 10 blog posts from the database
    blog_posts = BlogPost.objects.order_by('-date_posted')[:10]
    
    # Create a context dictionary to pass the blog posts to the template
    context = {
        'blog_posts': blog_posts
    }
    
    # context is passed to the template to be rendered
    return render(request, 'BlogApp/home.html', context)

# view to create a new blog post
def create_post(request):
    # Check if the form has been submitted
    if request.method == 'POST':
        # Create a new blog post
        new_post = BlogPost(
            # get the title and content from the form
            title = request.POST['title'],
            content = request.POST['content']
        )
        
        # Save the blog post to the database
        new_post.save()
        
        # Redirect to the home page
        return redirect('BlogApp:home')
    
    # If the form hasn't been submitted, display a blank form
    form = BlogPostForm()

    return render(request, 'BlogApp/createPost.html', {"form": form})

def view_post(request, post_id):
    # Retrieve the blog post from the database
    blog_post = BlogPost.objects.get(id=post_id)

    # Increment the view count
    blog_post.incremenetViewCount()

    # Create a context dictionary to pass the blog post to the template
    context = {
        'post': blog_post
    }
    
    # context is passed to the template to be rendered
    return render(request, 'BlogApp/viewPost.html', context)