from django.urls import path
from . import views

app_name = 'BlogApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('createPost', views.create_post, name='create_post'),
    path('viewPost/<int:post_id>', views.view_post, name='view_post'), # <int:post_id> is a dynamic path converter that converts the post_id to an integer and then passes it to the view_post function
]
