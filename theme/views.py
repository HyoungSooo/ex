from django.shortcuts import render

from django.views.generic import View, ListView, DetailView

from core.models import Post, Purpose, Professor, Timeline, AboutUs, Publictions

# Create your views here.


class AboutView(ListView):
    model = AboutUs
    template_name = 'team.html'
    context_object_name = 'about_us'

    def get_queryset(self):
        return AboutUs.objects.filter(category=self.kwargs['category'])


class PurposeView(ListView):
    model = Purpose
    template_name = 'purpose.html'
    context_object_name = 'purpose'


class PublicationsView(ListView):
    model = Publictions
    template_name = 'publications.html'
    context_object_name = 'publictions'


class PrincipleView(ListView):
    model = Professor
    template_name = 'principle.html'
    context_object_name = 'obj'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        if self.kwargs['category'] == 'news':
            return Post.objects.filter(category='News')
        elif self.kwargs['category'] == 'research':
            return Post.objects.filter(category='Research')
        else:
            return Post.objects.all()
