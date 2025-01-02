from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogListViews, BlogDetailView, BlogCreateView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListViews.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),

]
