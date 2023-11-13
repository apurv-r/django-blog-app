from django.db import models

# Create your models here.

from django.db import models

# creating a blog post model with a title, content, and date_posted fields
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True) #auto_now_add defaults the date_posted to the current date and time
    view_count = models.IntegerField(default=0) # default the view_count to 0

    def __str__(self): # returns the title of the blog post when the object is printed
        return self.title 

    def incremenetViewCount(self):
        self.view_count += 1
        self.save()