from django.urls import reverse_lazy

from blog.models import Blog
from django.views.generic import ListView, DetailView, CreateView, DeleteView


class BlogListViews(ListView):
    model = Blog
    template_name = 'blog_list.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.paginate_by:
            paginator = context['paginator']
            context['is_paginated'] = paginator.num_pages > 1
        return context


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'photo', 'content', 'is_published']
    success_url = reverse_lazy('blog:blog_list')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')

