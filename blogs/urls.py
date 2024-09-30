from django.urls import path
from . import views
app_name='blogs'
urlpatterns = [
    path('', views.homepage, name='homepage'),
     path('myblogs/', views.index, name='index'),
    path('blogs/<int:blog_id>/', views.blog, name="blog"),
    path('blogposts/<int:blogpost_id>/', views.blogpost, name='blogpost'),
    path('new_blog/', views.new_blog, name='new_blog'),
    path('new_blogpost/<int:blog_id>/', views.new_blogpost, name="new_blogpost" ),
    path('edit_blogpost/<int:blogpost_id>/', views.edit_blogpost, name='edit_blogpost'),

]